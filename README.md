# FitSense-XAI: Predicting Stress from Everyday Habits

This is my final-year project where I built a machine learning model that predicts stress levels from daily habits like sleep, physical activity, screen time, and diet.

Unlike most black-box models, this one explains *why* it made a prediction using **SHAP** (SHapley Additive exPlanations). The goal is to make AI more transparent and useful in real life.

---

## 🔗 Live Demo

👉 **Try the app here:** (https://fitsense-xai.streamlit.app)

Enter your own numbers and see what the model predicts for you.

---

## 📊 What's Inside

### Datasets Used
- **Wearable** (10,000 records): Sleep, activity, heart rate, stress
- **Student** (25,500 records): Academic pressure, sleep, social media
- **Lifestyle** (1,200 records): Diet, mood, physical activity

### Models Trained

| Model | Wearable | Student | Lifestyle |
|-------|----------|---------|-----------|
| Logistic Regression | 70.3% | 79.1% | **97.9%** |
| Random Forest | **85.9%** | **86.8%** | 96.3% |
| XGBoost | 83.2% | 85.9% | 97.1% |

**Best overall:** Random Forest (Wearable & Student), Logistic Regression (Lifestyle)

---

## 🧠 Why SHAP?

Most ML projects just give you a number — "your stress level is high". But I wanted to show *what factors* are driving that prediction.

SHAP helps the app tell you things like:
- "Your sleep quality is below average"
- "Your screen time is higher than usual"
- "You're not physically active enough"

This makes the model more **trustworthy** and **useful** in real life.

---

## 🛠️ Tech Stack

- **Python** (Pandas, NumPy)
- **Scikit-learn** (Random Forest, Logistic Regression)
- **XGBoost**
- **SMOTE** (for imbalanced data)
- **SHAP** (for explainability)
- **Streamlit** (for web app)
- **Matplotlib & Seaborn** (for visualizations)

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/tahsin1017/FitSense-XAI.git
cd FitSense-XAI
conda env create -f environment.yml
conda activate fitsense-env
streamlit run app/app.py
📁 Project Structure
FitSense-XAI/
├── app/                # Streamlit app
├── data/raw/           # Datasets
├── notebooks/          # Jupyter notebooks (EDA + training)
├── models/             # Saved models & SHAP explainers
├── reports/figures/    # Visualizations & SHAP plots
└── docs/               # Research journal (daily progress)
📌 What I Learned

Working with multiple datasets is messy but teaches you a lot about generalization.
SMOTE actually helps when your data is imbalanced.
SHAP makes ML models more usable and transparent.
Deploying a model as a web app changes how you think about the whole pipeline.
📄 License

MIT License — free for learning and research.

👤 Author

Tahsin Ahmed Rafi
Final Year CSE | Data Science & AI/ML
GitHub
