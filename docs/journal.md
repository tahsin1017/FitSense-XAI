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
