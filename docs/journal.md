# Research Journal - FitSense Project

## 📅 Day 1 (August 16, 2026)

### 🎯 Today's Objective:
- Complete the full project setup for FitSense
- Install all required packages
- Set up the development environment

### ✅ What I Accomplished:
1. **GitHub Repository:** Created `FitSense-XAI` repository (Public)
2. **Local Setup:** Cloned the repo to `~/Desktop/FitSense-XAI`
3. **Conda Environment:** Created `fitsense-env` with Python 3.10
4. **Packages Installed:**
   - numpy, pandas, matplotlib, seaborn, scikit-learn
   - xgboost
   - shap, lime (for explainability)
   - tensorflow (M1-optimized)
   - streamlit (for web app)
   - kaggle (for dataset download)
   - jupyter (for notebooks)
5. **Project Structure:** Created folders:
   - `data/raw/`, `data/processed/`
   - `notebooks/`
   - `src/`
   - `app/`
   - `models/`
   - `reports/figures/`
   - `docs/`
   - `scripts/`
6. **Configuration Files:** Created `requirements.txt` and `environment.yml`
7. **Kaggle Setup:** Configured Kaggle API and downloaded 3 datasets:
   - Wearable Tech: Sleep Quality & Stress Dataset
   - Mental Health Prediction Dataset
   - Synthetic Mental Health Dataset
8. **Zed Editor:** Installed and configured with the project
9. **Verification:** All packages imported successfully without errors

### 💡 Key Learnings Today:
- On M1 Mac, `tensorflow` (not `tensorflow-macos`) is the correct package
- Always activate the conda environment (`fitsense-env`) before working
- Kaggle API makes dataset downloading very convenient
- Zed is lightweight and perfect for M1 Mac (8GB RAM)

### ❌ Challenges Faced:
- Initially used wrong shell (bash), switched to zsh
- TensorFlow required the right version for M1
- SHAP and Streamlit were installed separately
- Needed to ensure `fitsense-env` was active, not `base`

### 🎯 Tomorrow's Plan (Day 2):
- Load all three datasets in Jupyter Notebook
- Explore each dataset's features and structure
- Check for missing values and data types
- Identify common features across datasets
- Start preliminary data visualization

### 📌 Current Status:
- ✅ Development environment: Ready
- ✅ All packages: Installed and working
- ✅ Datasets: Downloaded and ready
- ⏳ Data exploration: Pending (Day 2)

---

## 📅 Day 2 (August 19, 2026)

### 🎯 Today's Objective:
- Load and explore all three datasets
- Perform EDA (Exploratory Data Analysis)

### ✅ What I Accomplished:
1. Created `01_Data_Exploration.ipynb` in Jupyter
2. Loaded 3 datasets successfully:
   - Wearable: 10,000 rows, 16 columns
   - Student: 25,500 rows, 9 columns
   - Lifestyle: 1,200 rows, 7 columns
3. Explored each dataset (shape, columns, data types, missing values)
4. Found common features across datasets
5. Created distribution visualizations for all datasets
6. Identified correlations between features and stress levels

### 💡 Key Learnings:
- All 3 datasets have different column names but similar semantic meaning
- Wearable has most features (16) including BMI, heart rate, sleep quality
- Student has most records (25,500) but ~5% missing values
- Lifestyle is cleanest (0% missing) but smallest (1,200 records)

### ❌ Challenges Faced:
- Jupyter needed `python -m notebook` to run
- Seaborn installed via conda
- Reports folder needed to be created for saving figures

### 📌 Current Status:
- ✅ Data exploration complete
- ⏳ Data preprocessing: Pending (Day 3)

---

## 📅 Day 3 (August 19, 2026)

### 🎯 Today's Objective:
- Complete data preprocessing for all 3 datasets
- Handle missing values and categorical encoding
- Apply SMOTE for imbalanced data
- Scale features and split data for training

### ✅ What I Accomplished:

**1. EDA (Exploratory Data Analysis) - Final:**
- **Wearable Dataset:** 10,000 records, 16 features
  - Stress Distribution: Low (5,789), Medium (3,786), High (425) — Imbalanced
  - Sleep Quality Score: Range 1-7.5, mean 4.17
  - Top correlations: Sleep_Quality_Score (-0.47), Screen_Time_Hours (+0.29)
  
- **Student Dataset:** 25,500 records, 9 features
  - Stress Distribution: 70% Low, 30% High — Imbalanced
  - Missing Values: ~5% (handled with median imputation)
  - Top correlations: Exam_Pressure (+0.52), Sleep_Hours (-0.15)

- **Lifestyle Dataset:** 1,200 records, 7 features
  - Stress Distribution: Perfectly balanced (33.3% each)
  - No missing values
  - Top correlations: mood (-0.85), sleep_hours (-0.83)

**2. Data Preprocessing:**
- **Wearable Dataset:**
  - Encoded categorical columns: Gender, Diet_Type, Physical_Activity_Level
  - Encoded Daily_Stress_Level (Low=0, Medium=1, High=2)
  - Imputed 825 missing values with median
  - Applied SMOTE: 5,789 → 5,789 per class (balanced)
  - Scaled features using StandardScaler
  - Train/Test split: 13,893 / 3,474 samples

- **Student Dataset:**
  - Imputed missing values with median
  - Encoded Student_Type (Label Encoding)
  - Applied SMOTE: 17,853 → 17,853 per class (balanced)
  - Scaled features using StandardScaler
  - Train/Test split: 28,564 / 7,142 samples

- **Lifestyle Dataset:**
  - Already balanced, no SMOTE needed
  - Scaled features using StandardScaler
  - Train/Test split: 960 / 240 samples

**3. Visualizations Saved:**
- `reports/figures/stress_distribution_comparison.png`
- `reports/figures/correlation_heatmaps.png`

### 💡 Key Learnings Today:
- Sleep quality and physical activity are strongest negative predictors of stress
- Screen time and exam pressure positively correlate with stress
- SMOTE is effective for handling imbalanced datasets
- Feature scaling is essential before model training
- All categorical data must be numeric before applying SMOTE

### ❌ Challenges Faced:
- `Physical_Activity_Level` was string type → encoded to numeric
- X1 had 825 NaN values → imputed with median
- SMOTE required all features to be numeric with no NaN

### 🎯 Tomorrow's Plan (Day 4):
- Train baseline models on all 3 datasets
- Compare performance (Accuracy, Precision, Recall, F1-Score)
- Implement Explainable AI (SHAP) for model interpretability
- Start writing the research paper draft

### 📌 Current Status:
- ✅ EDA Complete
- ✅ Data Preprocessing Complete
- ✅ All datasets balanced (SMOTE applied)
- ✅ Features Scaled
- ✅ Train/Test Split Complete
- ⏳ Model Training: Pending (Day 4)

---

## 📅 Day 4 (August 20, 2026)

### 🎯 Today's Objective:
- Train baseline models on all 3 datasets
- Evaluate model performance using multiple metrics
- Implement Explainable AI (SHAP) for model interpretability
- Save all models and SHAP explainers for future use

### ✅ What I Accomplished:

**1. Model Training (3 Models × 3 Datasets):**

| Model | Wearable (Accuracy) | Student (Accuracy) | Lifestyle (Accuracy) |
|-------|---------------------|--------------------|----------------------|
| Logistic Regression | 0.7026 | 0.7908 | 0.9792 |
| Random Forest | 0.8359 | 0.8682 | 0.9625 |
| XGBoost | 0.8325 | 0.8589 | 0.9708 |

**Best Model per Dataset:**
- **Wearable:** Random Forest (Accuracy: 0.8359, F1: 0.8340)
- **Student:** Random Forest (Accuracy: 0.8682, F1: 0.8682)
- **Lifestyle:** Logistic Regression (Accuracy: 0.9792, F1: 0.9792)

**2. Model Evaluation:**
- Calculated Accuracy, Precision, Recall, and F1-Score for all models
- Generated Confusion Matrices for best models
- Saved best models as `.pkl` files in `models/` folder

**3. Explainable AI (SHAP) Implementation:**
- Used `shap.TreeExplainer` for Random Forest models (Wearable, Student)
- Used `shap.LinearExplainer` for Logistic Regression model (Lifestyle)
- Generated SHAP Summary Plots for all 3 datasets
- Generated SHAP Feature Importance (Bar) Plots for all 3 datasets
- Generated SHAP Waterfall Plots for Wearable dataset (all 3 classes)

**4. Files Saved:**
- `notebooks/02_Model_Training.ipynb`
- `models/best_wearable_model.pkl`
- `models/best_student_model.pkl`
- `models/best_lifestyle_model.pkl`
- `models/shap_explainer_Wearable.pkl`
- `models/shap_explainer_Student.pkl`
- `models/shap_explainer_Lifestyle.pkl`
- `reports/figures/model_comparison.png`
- `reports/figures/confusion_matrices.png`
- `reports/figures/shap_summary_Wearable.png`
- `reports/figures/shap_importance_Wearable.png`
- `reports/figures/shap_summary_Student.png`
- `reports/figures/shap_importance_Student.png`
- `reports/figures/shap_summary_Lifestyle.png`
- `reports/figures/shap_importance_Lifestyle.png`
- `reports/figures/shap_waterfall_wearable.png`
- `reports/figures/shap_waterfall_wearable_class_0.png` (Low Stress)
- `reports/figures/shap_waterfall_wearable_class_1.png` (Medium Stress)
- `reports/figures/shap_waterfall_wearable_class_2.png` (High Stress)

### 💡 Key Learnings Today:
- Random Forest performed consistently well across all datasets
- Logistic Regression achieved 97.9% accuracy on Lifestyle dataset (cleanest data)
- SMOTE helped improve model performance on imbalanced datasets
- SHAP successfully identified key predictors:
  - **Wearable:** Sleep_Quality_Score and Daily_Sleep_Hours
  - **Student:** Exam_Pressure and Study_Hours
  - **Lifestyle:** sleep_hours and mood
- For multi-class classification, SHAP returns `(samples, features, classes)` shape
- Waterfall plots need class index selection for multi-class models

### ❌ Challenges Faced:
- XGBoost needed `num_class` parameter for multi-class classification
- XGBoost required `binary:logistic` for binary classification (Student dataset)
- SHAP `ax` parameter not supported in newer versions → saved individual figures
- `shap.TreeExplainer` doesn't work with Logistic Regression → used `shap.LinearExplainer`

### 🎯 Tomorrow's Plan (Day 5):
- Build Streamlit web application for model deployment
- Create user input form for predictions
- Display predictions with SHAP explanations
- Deploy app on Streamlit Cloud

### 📌 Current Status:
- ✅ Model Training Complete
- ✅ Model Evaluation Complete
- ✅ SHAP Explainability Complete
- ✅ All SHAP Figures Saved
- ✅ Best Models Saved
- ✅ SHAP Explainers Saved
- ⏳ Streamlit App: Pending (Day 5)

---

## 📅 Day 5 (August 20, 2026)

### 🎯 Today's Objective:
- Build and deploy Streamlit web application
- Create interactive user input form with 14 features
- Display predictions with confidence scores
- Provide lifestyle-based recommendations

### ✅ What I Accomplished:

**1. Streamlit App Development:**
- Created `app/app.py` with 14 input features
- Added sliders for numeric inputs and dropdowns for categorical features
- Integrated trained Random Forest model and scaler
- Added real-time prediction with confidence scores
- Displayed probability distribution bar chart

**2. Feature Inputs (14 Features):**
- Numeric: Age, BMI, Caffeine Intake, Water Intake, Screen Time, Daily Steps, Calories Burned, Resting Heart Rate, Daily Sleep Hours, Deep Sleep Hours, Sleep Quality Score
- Categorical: Gender, Diet Type, Physical Activity Level

**3. User Experience Features:**
- Personalized lifestyle explanations based on input values
- Actionable recommendations to reduce stress
- Clean, professional UI with Streamlit
- Mobile-responsive layout

**4. Error Handling:**
- Fixed `IndexError` by converting `pred` to `int` for indexing
- Added debug mode for troubleshooting
- Graceful error handling with traceback display

**5. Files Created:**
- `app/app.py` - Main Streamlit application
- `models/best_wearable_model_14features.pkl` - Retrained model with 14 features
- `models/scaler_wearable_14features.pkl` - Scaler for 14 features
- `models/shap_explainer_Wearable_14features.pkl` - SHAP explainer for 14 features

### 💡 Key Learnings Today:
- Feature order between training and inference must match exactly
- `scaler.transform()` expects the same feature format as training
- `numpy.int64` cannot be used directly as array index → convert to `int`
- Streamlit's `st.cache_resource` is useful for loading large models
- UI/UX matters for research projects

### ❌ Challenges Faced:
- SHAP waterfall plot errors in Streamlit (IndexError with `numpy.int64`)
- Feature format mismatch between training and inference
- Need to convert `pred` to `int` before using as array index
- Debugging Streamlit apps requires careful error tracing

### 🎯 Next Steps:
- Deploy app on Streamlit Cloud
- Write research paper
- Add more datasets for validation
- Implement real-time SHAP explanation

### 📌 Current Status:
- ✅ Streamlit App Complete
- ✅ All 14 Features Working
- ✅ Predictions with Confidence
- ✅ Lifestyle Recommendations
- ✅ Error Handling Complete
- ⏳ Cloud Deployment: Pending
