import streamlit as st
import numpy as np
import pandas as pd
import joblib
import os
import traceback

st.set_page_config(page_title="FitSense - Stress Predictor", layout="wide")

st.title("🧠 FitSense: Mental Health & Physical Activity Analyzer")
st.markdown("Predict your stress level based on your physical activity, sleep, and lifestyle habits.")

@st.cache_resource
def load_model_and_scaler():
    try:
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        models_path = os.path.join(base_path, 'models')
        model = joblib.load(os.path.join(models_path, 'best_wearable_model_14features.pkl'))
        scaler = joblib.load(os.path.join(models_path, 'scaler_wearable_14features.pkl'))
        return model, scaler
    except Exception as e:
        st.error(f"Error loading models: {e}")
        return None, None

model, scaler = load_model_and_scaler()

if model is None:
    st.warning("⚠️ Please train the 14-feature model first using the Jupyter notebook.")
    st.stop()

st.sidebar.header("📊 Enter Your Data")

age = st.sidebar.slider("Age", 18, 80, 30)
bmi = st.sidebar.slider("BMI", 15.0, 40.0, 22.5)
caffeine = st.sidebar.slider("Caffeine Intake (mg)", 0, 500, 100)
water = st.sidebar.slider("Water Intake (liters)", 0.0, 5.0, 2.0)
screen_time = st.sidebar.slider("Screen Time (hours)", 0.0, 12.0, 4.0)
steps = st.sidebar.slider("Daily Steps", 1000, 15000, 7000)
calories = st.sidebar.slider("Calories Burned", 500, 3000, 1500)
heart_rate = st.sidebar.slider("Resting Heart Rate (bpm)", 50, 100, 70)
sleep_hours = st.sidebar.slider("Daily Sleep (hours)", 3.0, 10.0, 7.0)
deep_sleep = st.sidebar.slider("Deep Sleep (hours)", 0.5, 4.0, 2.0)
sleep_quality = st.sidebar.slider("Sleep Quality Score", 1.0, 10.0, 6.0)

gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"])
diet = st.sidebar.selectbox("Diet Type", ["Average", "Healthy", "Unhealthy"])
activity = st.sidebar.selectbox("Physical Activity Level", ["Low", "Medium", "High"])

gender_map = {'Female': 0, 'Male': 1, 'Other': 2}
diet_map = {'Average': 0, 'Healthy': 1, 'Unhealthy': 2}
activity_map = {'Low': 0, 'Medium': 1, 'High': 2}

input_data = np.array([[
    age, bmi, caffeine, water, screen_time, steps, calories,
    heart_rate, sleep_hours, deep_sleep, sleep_quality,
    gender_map[gender], diet_map[diet], activity_map[activity]
]])

if st.sidebar.button("🔮 Predict Stress Level"):
    try:
        input_scaled = scaler.transform(input_data)
        pred = model.predict(input_scaled)[0]
        proba = model.predict_proba(input_scaled)[0]

        # FIX: Convert pred to int for indexing
        pred_int = int(pred)

        stress_map = {0: "Low 😊", 1: "Medium 😐", 2: "High 😰"}
        stress_label = stress_map[pred_int]

        st.subheader("📈 Prediction Result")
        col1, col2, col3 = st.columns(3)
        col1.metric("Stress Level", stress_label)
        col2.metric("Confidence", f"{proba[pred_int]*100:.1f}%")
        col3.metric("Risk", "⚠️ High" if pred_int == 2 else "⚠️ Medium" if pred_int == 1 else "✅ Low")

        prob_df = pd.DataFrame({'Stress Level': ['Low', 'Medium', 'High'], 'Probability': proba})
        st.bar_chart(prob_df.set_index('Stress Level'))

        st.subheader("💡 How your lifestyle affects stress")
        explanations, recommendations = [], []

        if sleep_quality < 5:
            explanations.append(f"🛌 Sleep quality: {sleep_quality:.1f}/10 (below average)")
            recommendations.append("🛌 Improve sleep quality: maintain regular sleep schedule")
        elif sleep_quality >= 7:
            explanations.append(f"🛌 Sleep quality: {sleep_quality:.1f}/10 (good!)")
        if sleep_hours < 6:
            explanations.append(f"😴 Sleep: {sleep_hours:.1f} hours (below recommended 7-8 hours)")
            recommendations.append("😴 Try to sleep 7-8 hours daily")
        elif sleep_hours >= 7:
            explanations.append(f"😴 Sleep: {sleep_hours:.1f} hours (healthy range)")
        if activity == "Low":
            explanations.append("🏃 Physical activity: Low")
            recommendations.append("🏃 Exercise 3-4 times per week")
        elif activity == "Medium":
            explanations.append("🏃 Physical activity: Medium (good!)")
        else:
            explanations.append("🏃 Physical activity: High (excellent!)")
        if screen_time > 6:
            explanations.append(f"📱 Screen time: {screen_time:.1f} hours/day (high)")
            recommendations.append("📱 Limit screen time to 4-5 hours")
        elif screen_time <= 4:
            explanations.append(f"📱 Screen time: {screen_time:.1f} hours/day (good)")
        if steps < 5000:
            explanations.append(f"🚶 Steps: {steps:,} (below 5,000)")
            recommendations.append("🚶 Aim for 7,000-10,000 steps daily")
        elif steps >= 7000:
            explanations.append(f"🚶 Steps: {steps:,} (good!)")
        if bmi > 25:
            explanations.append(f"⚖️ BMI: {bmi:.1f} (above healthy range)")
            recommendations.append("⚖️ Maintain healthy BMI through diet and exercise")
        elif bmi < 18.5:
            explanations.append(f"⚖️ BMI: {bmi:.1f} (below healthy range)")
            recommendations.append("⚖️ Ensure adequate nutrition")
        else:
            explanations.append(f"⚖️ BMI: {bmi:.1f} (healthy range)")

        st.write("**Your current lifestyle:**")
        for exp in explanations:
            st.write(f"- {exp}")
        if recommendations:
            st.write("**📋 Recommendations to reduce stress:**")
            for rec in recommendations:
                st.write(f"- {rec}")
        else:
            st.success("✅ Your lifestyle is healthy! Keep it up!")

    except Exception as e:
        st.exception(traceback.format_exc())

st.markdown("---")
st.caption("🧠 FitSense-XAI | Built with Streamlit & Machine Learning")
st.caption("📊 SHAP analysis available in the research notebook and reports folder")
