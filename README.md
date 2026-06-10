# 🤖 Machine Learning Journey

> A complete, hands-on repository documenting my Machine Learning learning path — from absolute beginner to building real-world projects with deployable web apps.

I started this journey with very little knowledge, following the **100 Days of Machine Learning** course, and have been building up concepts, notes, and projects one step at a time. This repo reflects real progress — messy at times, but honest and continuous.

---

## 📁 Repository Structure

```
Machine Learning/
│
├── 📊 Understanding of Data/          # EDA, Pandas Profiling
├── 🗂️ Working with File Types/        # CSV, JSON, SQL, APIs, Web Scraping
├── 🔧 Features Engineering/           # Encoding, Scaling, Imputation, Transformation
├── 🧮 Algorithms/                     # All ML algorithms with notebooks
│   ├── Linear Regression/
│   ├── Logistic Regression/
│   ├── Naive Bayes/
│   ├── KNN/
│   ├── SVM/
│   ├── Ensemble Learning/
│   └── ...
├── 🔩 Pipeline/                       # Sklearn Pipelines with Titanic dataset
├── 🚀 ML Projects/                    # End-to-end projects
└── 🧪 Practice/                       # Practice notebooks
```

---

## 🧠 What I've Learned & Covered

### 📊 Understanding of Data
- Exploratory Data Analysis (EDA)
- Pandas Profiling
- Univariate & Bivariate Analysis

### 🗂️ Working with File Types
| Type | Notebook |
|------|----------|
| CSV Files | `Working with CSV.ipynb` |
| JSON & SQL | `JSON SQl.ipynb` |
| APIs | `API.ipynb` |
| Web Scraping | `Web Scraping.ipynb` |

---

### 🔧 Feature Engineering

#### Missing Value Imputation
- Complete Case Analysis (CCA)
- Mean / Median / Mode Imputation
- Random Sample Imputation
- KNN & Iterative Imputer

#### Feature Encoding
- One Hot Encoding
- Ordinal Encoding
- Label Encoding
- Target Encoding

#### Feature Scaling & Transformation
- Normalization
- Standardization
- Binarization
- Discretization (Binning)
- Function Transformation (Log, Square Root, Reciprocal)
- Power Transformation (Box-Cox, Yeo-Johnson)
- Column Transformer

#### Outlier Handling
- Z-score Method
- IQR Method

#### Feature Construction & Selection
- Feature Construction
- Feature Splitting
- Time-based Feature Extraction
- PCA (Principal Component Analysis) — from scratch and with Sklearn

---

### 🧮 Algorithms

#### Linear Regression
- Simple Linear Regression (with Formula from scratch)
- Multiple Linear Regression
- Polynomial Linear Regression
- Error Metrics: MAE, MSE, RMSE, R², Adjusted R²

#### Gradient Descent
- Batch Gradient Descent
- Stochastic Gradient Descent (SGD)
- Mini-Batch Gradient Descent
- Gradient Descent Step-by-Step from scratch

#### Bias-Variance Tradeoff & Regularization
- Ridge Regression (from scratch + Gradient Descent)
- Lasso Regression
- ElasticNet Regression

#### Logistic Regression
- Sigmoid Function
- Perceptron Trick
- Softmax Regression
- Logistic Regression from scratch

#### Naive Bayes
- Gaussian Naive Bayes
- Multinomial Naive Bayes
- Bernoulli Naive Bayes

#### K-Nearest Neighbors (KNN)

#### Support Vector Machine (SVM)

#### Ensemble Learning
| Method | Notebooks |
|--------|-----------|
| Decision Tree | Classification + Regression Tree, dtreeviz visualization |
| Random Forest | Classification, Regression, OOB Score |
| Bagging | Demo, Regression, Learning Tool |
| AdaBoost | From scratch + with Sklearn |
| Gradient Boosting | Step-by-step from scratch |
| Voting Classifier | Hard & Soft Voting, Voting Regression |
| Stacking & Blending | Stacking on Heart Disease Dataset |

---

### 🔩 Pipeline
- Building Sklearn Pipelines
- Titanic Survival Prediction with and without Pipeline
- Saving and loading Pipeline models (`.pkl`)

---

## 🚀 ML Projects

### 1. 🎓 Placement Prediction *(First Project)*
> Built early in the journey (~Day 13) to understand the end-to-end ML workflow.
- Simple Linear Regression on placement dataset
- Deployed as a web app using Flask
- **Files:** `Placement.ipynb`, `app.py`, `model.pkl`

### 2. 🚢 Titanic Survival Prediction
- Classification with preprocessing pipeline
- Flask web app for prediction
- **Files:** `Titanic prediction.ipynb`, `app.py`, `titanic.pkl`

### 3. 📞 Customer Churn Prediction
- Telecom customer churn analysis
- Feature engineering + classification
- **Dataset:** Telco Customer Churn (IBM)
- **Files:** `Customer Churn.ipynb`

### 4. 👔 Employee Attrition Prediction System
- Predicts whether an employee will leave the company
- Full pipeline with preprocessing
- Flask web app with live prediction
- **Files:** `Employee Attrition Prediction System.ipynb`, `app.py`, `model.pkl`

### 5. 💰 Credit Risk Prediction
- Loan risk classification with hyperparameter tuning
- Confusion matrix & ROC-AUC evaluation
- Deployed as a Flask web app
- **Files:** `credit-risk-prediction.ipynb`, `app.py`, `credit-risk-prediction.pkl`

### 6. 📢 Advertising Sales Prediction
- Predict sales from advertising spend (TV, Radio, Newspaper)
- **Files:** `Advertising Sales Prediction.ipynb`

### 7. 🤖 AutoML System *(Work in Progress)*
- Modular AutoML pipeline with separate components:
  - Data loading, EDA, preprocessing
  - Model selection, hyperparameter tuning
  - Ensemble methods, imbalance handling
  - Evaluation & recommendation
- **Datasets Used:** Telco Churn, Loan Risk

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-yellowgreen?logo=scikit-learn)
![Pandas](https://img.shields.io/badge/Pandas-Data-purple?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Array-lightblue?logo=numpy)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Viz-red)

**Libraries used across the repo:**
- `pandas`, `numpy` — Data manipulation
- `matplotlib`, `seaborn`, `plotly` — Visualization
- `scikit-learn` — ML models, pipelines, preprocessing
- `flask` — Web app deployment
- `ydata-profiling` (pandas-profiling) — Auto EDA reports
- `dtreeviz` — Decision tree visualization
- `pickle` — Model serialization

---

## 📈 Learning Source

- 📺 [100 Days of Machine Learning – CampusX (YouTube)](https://www.youtube.com/@campusx-official)
- 🧪 Self-practice, experimentation, and building from scratch
- 📝 Personal notes and documentation alongside each concept

---

## 🗓️ Progress Timeline

| Phase | Topics Covered |
|-------|---------------|
| Days 1–15 | Python basics, Data loading, First project (Placement Prediction) |
| Days 16–25 | File types (CSV, JSON, SQL, API, Web Scraping) |
| Days 26–50 | Feature Engineering (Encoding, Scaling, Imputation, Transformation) |
| Days 51–70 | Linear & Logistic Regression, Gradient Descent, Regularization |
| Days 71–85 | Naive Bayes, KNN, SVM, Decision Tree |
| Days 86–100 | Ensemble Learning, Pipelines, Advanced Projects |
| Ongoing | AutoML, deeper projects, deployment |

---

## 📌 How to Use This Repo

1. **Clone the repo**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Machine-Learning.git
   cd Machine-Learning
   ```

2. **Install dependencies**
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn flask ydata-profiling jupyter
   ```

3. **Open any notebook**
   ```bash
   jupyter notebook
   ```

4. **Run a project web app** (e.g. Credit Risk)
   ```bash
   cd "ML Projects/Credit Risk Prediction"
   pip install -r requirements.txt
   python app.py
   ```

---

## 🙌 About

This repository is my open learning journal. Every notebook, dataset, and project reflects real practice and progression. If you're also learning ML, feel free to explore, fork, or use anything here!

> *"The best way to learn is to build."*

---

⭐ **Star this repo if you find it helpful!**
