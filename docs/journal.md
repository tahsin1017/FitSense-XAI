# Research Journal - FitSense Project

---

## 📅 Day 1 (August 16, 2026)

### 🎯 Today's Goal:
- Set up the project environment and download datasets

### ✅ What I Did:
- Created GitHub repo (`FitSense-XAI`) and cloned it locally
- Set up conda environment (`fitsense-env`) with Python 3.10
- Installed all required packages (numpy, pandas, sklearn, xgboost, shap, streamlit, etc.)
- Created project folder structure (data/, notebooks/, src/, app/, models/, reports/, docs/)
- Configured Kaggle API and downloaded 3 datasets (Wearable, Student, Lifestyle)

### 💡 What I Learned:
- On M1 Mac, use `tensorflow` (not `tensorflow-macos`)
- Always activate conda environment before working
- Zed is lighter than VS Code for 8GB RAM

### ⚠️ Issues I Ran Into:
- Started with bash shell, switched to zsh
- TensorFlow version needed fixing for M1
- Had to install shap and streamlit separately

### 📌 Where I Stand:
- ✅ Environment ready
- ✅ All packages installed
- ✅ Datasets downloaded
- ⏳ Data exploration starts tomorrow

---

## 📅 Day 2 (August 19, 2026)

### 🎯 Today's Goal:
- Explore the datasets and understand what I'm working with

### ✅ What I Did:
- Created `01_Data_Exploration.ipynb` in Jupyter
- Loaded all 3 datasets:
  - Wearable: 10k rows, 16 columns
  - Student: 25.5k rows, 9 columns
  - Lifestyle: 1.2k rows, 7 columns
- Checked data types, missing values, and distributions
- Created visualizations for each dataset
- Found correlations between features and stress levels

### 💡 What I Noticed:
- All datasets have different column names but similar meaning
- Wearable has the most features (BMI, heart rate, sleep quality)
- Student has the most records but ~5% missing values
- Lifestyle is clean but small

### ⚠️ Issues I Ran Into:
- Jupyter needed `python -m notebook` to run
- Had to install seaborn via conda
- Created reports folder for saving figures

### 📌 Where I Stand:
- ✅ Data exploration done
- ⏳ Preprocessing starts tomorrow

---

## 📅 Day 3 (August 19, 2026)

### 🎯 Today's Goal:
- Clean the data and get it ready for modeling

### ✅ What I Did:

**Data exploration summary:**
- Wearable: 10k records, stress imbalanced (Low: 58%, Medium: 38%, High: 4%)
- Student: 25.5k records, 70% Low stress, 30% High stress
- Lifestyle: 1.2k records, perfectly balanced (33% each)

**Preprocessing work:**
- Encoded categorical columns (Gender, Diet_Type, Physical_Activity_Level)
- Encoded stress labels (Low=0, Medium=1, High=2)
- Imputed 825 missing values with median
- Applied SMOTE to balance the data
- Scaled features using StandardScaler
- Split data into train/test (80/20)

### 💡 What I Learned:
- Sleep quality and physical activity are strong negative predictors of stress
- Screen time and exam pressure increase stress
- SMOTE actually helps with imbalanced data
- Feature scaling is important before model training

### ⚠️ Issues I Ran Into:
- `Physical_Activity_Level` was string → had to encode it
- Found 825 NaN values → imputed with median
- SMOTE needs all features to be numeric

### 📌 Where I Stand:
- ✅ EDA done
- ✅ Preprocessing done
- ✅ Data balanced and scaled
- ✅ Train/test split ready
- ⏳ Model training tomorrow

---

## 📅 Day 4 (August 20, 2026)

### 🎯 Today's Goal:
- Train models and add explainability (SHAP)

### ✅ What I Did:

**Trained 3 models on all datasets:**

| Model | Wearable | Student | Lifestyle |
|-------|----------|---------|-----------|
| Logistic Regression | 70.3% | 79.1% | 97.9% |
| Random Forest | 85.9% | 86.8% | 96.3% |
| XGBoost | 83.2% | 85.9% | 97.1% |

**Best model for each:**
- Wearable: Random Forest (85.9%)
- Student: Random Forest (86.8%)
- Lifestyle: Logistic Regression (97.9%)

**Added SHAP explainability:**
- Generated SHAP summary plots for all 3 datasets
- Created feature importance plots
- Made waterfall plots for Wearable dataset (all 3 stress classes)

**Saved everything:**
- Models, scalers, and SHAP explainers as `.pkl` files
- All figures in `reports/figures/`

### 💡 What I Learned:
- Random Forest works well across different datasets
- Clean data (Lifestyle) gave 97.9% accuracy with simple Logistic Regression
- SHAP showed that sleep is the strongest predictor of stress

### ⚠️ Issues I Ran Into:
- XGBoost needed `num_class` for multi-class
- SHAP `ax` parameter not supported in newer versions → saved individual figures
- Used `shap.LinearExplainer` for Logistic Regression (TreeExplainer doesn't work)

### 📌 Where I Stand:
- ✅ Models trained and evaluated
- ✅ SHAP explainability done
- ✅ All models and explainers saved
- ⏳ Building the web app tomorrow

---

## 📅 Day 5 (August 20, 2026)

### 🎯 Today's Goal:
- Build a web app and deploy it online

### ✅ What I Did:

**Built Streamlit app (`app/app.py`):**
- Added 14 input features (age, BMI, sleep, activity, screen time, etc.)
- Integrated trained Random Forest model
- Shows prediction with confidence score
- Displays probability distribution chart
- Gives lifestyle recommendations based on user inputs

**Fixed errors:**
- Converted `pred` to `int` for array indexing
- Added proper error handling
- Fixed feature order mismatch between training and inference

**Deployed on Streamlit Cloud:**
- App is live at: https://fitsense-xai.streamlit.app
- Updated README with live demo link
- Updated this journal

### 💡 What I Learned:
- Feature order must match exactly between training and inference
- `numpy.int64` can't be used directly as array index → convert to `int`
- `st.cache_resource` is useful for loading models
- Deploying changes how you think about the whole pipeline

### ⚠️ Issues I Ran Into:
- SHAP waterfall plots kept throwing errors in Streamlit
- Feature format mismatch between training and app input
- Took a while to figure out the array indexing issue

### 📌 Where I Stand:
- ✅ Web app built
- ✅ All 14 features working
- ✅ App deployed and live
- ✅ README updated
- ✅ GitHub repo ready
- ⏳ Next: Write the research paper

---

**GitHub:** https://github.com/tahsin1017/FitSense-XAI  
**Live App:** https://fitsense-xai.streamlit.app
