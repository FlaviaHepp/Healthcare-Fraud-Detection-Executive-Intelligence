# 🐍 Python — Machine Learning & Fraud Intelligence Pipeline

This folder contains the Python workflow used for data preparation, exploratory analysis, machine learning, explainability, business analysis, and result export.

---

## 🎯 Objective

Build a reproducible fraud detection workflow capable of:

- Preparing healthcare claims data
- Exploring distributions and fraud patterns
- Engineering predictive features
- Comparing classification models
- Optimizing model hyperparameters
- Evaluating predictive performance
- Explaining predictions
- Exporting results for downstream analytics

---

## 🔬 Workflow

```text
Data Loading
    ↓
Data Quality & Preprocessing
    ↓
Exploratory Data Analysis
    ↓
Feature Engineering
    ↓
Model Preparation
    ↓
Model Benchmarking
    ↓
Hyperparameter Optimization
    ↓
Model Evaluation
    ↓
Explainable AI
    ↓
Business Insights
    ↓
Result Export
```

---

## 🤖 Models

The project evaluates:

- Logistic Regression
- Random Forest
- XGBoost
- LightGBM
- CatBoost

The purpose of benchmarking several algorithms is to compare their behavior under the same analytical problem rather than relying on a single model.

---

## 📊 Evaluation Metrics

The workflow includes:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Confusion Matrix
- ROC Curve

Fraud detection requires attention to both false positives and false negatives, so multiple metrics are considered together.

---

## 🧠 Explainable AI

SHAP is used to analyze feature contributions and answer questions such as:

> Which variables contributed most to a fraud prediction?

This creates a bridge between:

```text
Model Prediction
      ↓
Feature Contribution
      ↓
Fraud Intelligence
```

---

## 📦 Result Export

The export workflow produces structured outputs such as:

```text
model_metrics.csv
ml_predictions.csv
confusion_matrix.csv
roc_curve.csv
feature_importance.csv
high_risk_claims.csv
shap_values.csv
```

These files are stored in the repository's `results/` directory.

The current export script writes these files to an `outputs` directory during local execution; for the GitHub structure, generated deliverables should be moved or copied into `results/`.

---

## 🗃️ Data

The main input dataset used by the workflow is:

```text
healthcare_fraud_detection.csv
```

Recommended repository location:

```text
data/raw/healthcare_fraud_detection.csv
```

When the dataset is available under that path, the Python scripts should use the repository-relative path rather than a machine-specific absolute path.

---

## 🛠️ Main Libraries

- Pandas
- NumPy
- Scikit-learn
- XGBoost
- LightGBM
- CatBoost
- SHAP
- Matplotlib
- Seaborn
- Joblib

---

## ▶️ Reproducibility

Run the workflow from the repository root so relative paths resolve consistently.

Recommended order:

```text
1. Load data
2. Validate / preprocess
3. Explore
4. Engineer features
5. Train models
6. Evaluate
7. Tune
8. Explain
9. Export results
```

---

## 🔗 Connection to Other Layers

```text
Python
   │
   ├── models/     → trained model artifacts
   │
   └── results/    → metrics, predictions and explainability outputs
                         │
                         ▼
                       SQL
                         │
                         ▼
                    Power BI
```

Python is therefore the main predictive and analytical layer of the project.
