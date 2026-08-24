# ==========================================================
# BLOCK 12 - EXPORT RESULTS FOR POWER BI
# Healthcare Fraud Detection & Executive Intelligence
# ==========================================================

import warnings
warnings.filterwarnings("ignore")

import os
import joblib
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    roc_curve
)

print("=" * 80)
print("EXPORT RESULTS")
print("=" * 80)

# ==========================================================
# OUTPUT FOLDER
# ==========================================================

OUTPUT_FOLDER = "outputs"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ==========================================================
# LOAD DATASET
# ==========================================================

DATA_PATH = "healthcare_fraud_detection.csv"

df = pd.read_csv(DATA_PATH)

print(f"Dataset loaded: {df.shape}")

# Guardamos el Claim_ID para exportarlo después
claim_ids = df["Claim_ID"].copy()

# ==========================================================
# COPY DATASET
# ==========================================================

model_df = df.copy()

# ==========================================================
# REMOVE COLUMNS
# ==========================================================

columns_to_drop = [

    "Claim_ID",
    "Patient_ID",
    "Provider_ID",

    "Claim_Submission_Date",
    "Service_Date",

    "Provider_Historical_Fraud_Rate"

]

for col in columns_to_drop:
    if col in model_df.columns:
        model_df.drop(columns=col, inplace=True)

print("\nColumns removed:")
print(columns_to_drop)

# ==========================================================
# LABEL ENCODER
# ==========================================================

categorical_cols = model_df.select_dtypes(
    include=["object", "category"]
).columns

encoders = {}

for col in categorical_cols:

    encoder = LabelEncoder()

    model_df[col] = encoder.fit_transform(
        model_df[col].astype(str)
    )

    encoders[col] = encoder

print(f"\nCategorical variables encoded: {len(categorical_cols)}")

# ==========================================================
# FEATURES & TARGET
# ==========================================================

X = model_df.drop("Is_Fraud", axis=1)

y = model_df["Is_Fraud"]

print("\nX Shape:", X.shape)
print("y Shape:", y.shape)

# ==========================================================
# TRAIN TEST SPLIT
# ==========================================================

X_train, X_test, y_train, y_test, claim_train, claim_test = train_test_split(

    X,
    y,
    claim_ids,

    test_size=0.20,

    random_state=42,

    stratify=y

)

print("\nTrain:", X_train.shape)
print("Test :", X_test.shape)

# ==========================================================
# IMPUTATION
# ==========================================================

imputer = SimpleImputer(strategy="median")

X_train = pd.DataFrame(

    imputer.fit_transform(X_train),

    columns=X_train.columns

)

X_test = pd.DataFrame(

    imputer.transform(X_test),

    columns=X_test.columns

)

# ==========================================================
# STANDARD SCALER
# ==========================================================

scaler = StandardScaler()

X_train_scaled = X_train.copy()

X_test_scaled = X_test.copy()

numeric_columns = X_train.columns

X_train_scaled[numeric_columns] = scaler.fit_transform(X_train)

X_test_scaled[numeric_columns] = scaler.transform(X_test)

print("\nPreprocessing completed.")

# ==========================================================
# LOAD TRAINED MODEL
# ==========================================================

print("\nLoading trained model...")

MODEL_PATH = "best_healthcare_fraud_model.pkl"

best_model = joblib.load(MODEL_PATH)

print("Model loaded successfully.")

# ==========================================================
# DETECT MODEL TYPE
# ==========================================================

model_name = type(best_model).__name__

print(f"Detected model: {model_name}")

# ==========================================================
# SELECT CORRECT DATA
# ==========================================================

if model_name == "LogisticRegression":

    X_eval = X_test_scaled

else:

    X_eval = X_test

# ==========================================================
# PREDICTIONS
# ==========================================================

pred = best_model.predict(X_eval)

prob = best_model.predict_proba(X_eval)[:, 1]

print("Predictions generated.")

# ==========================================================
# MODEL METRICS
# ==========================================================

# ==========================================================
# MODEL METRICS
# ==========================================================

# ==========================================================
# EXPORT MODEL METRICS
# ==========================================================

print("\nExporting model metrics...")

# ----------------------------------------------------------
# Calculate metrics
# ----------------------------------------------------------

accuracy = float(accuracy_score(y_test, pred))
precision = float(precision_score(y_test, pred))
recall = float(recall_score(y_test, pred))
f1 = float(f1_score(y_test, pred))
roc_auc = float(roc_auc_score(y_test, prob))

# ----------------------------------------------------------
# Create DataFrame
# ----------------------------------------------------------

metrics = pd.DataFrame({

    "Metric": [

        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "ROC AUC"

    ],

    "Value": [

        round(accuracy, 4),
        round(precision, 4),
        round(recall, 4),
        round(f1, 4),
        round(roc_auc, 4)

    ]

})

# ----------------------------------------------------------
# Export CSV compatible with Power BI (Spanish locale)
# ----------------------------------------------------------

metrics.to_csv(

    os.path.join(
        OUTPUT_FOLDER,
        "model_metrics.csv"
    ),

    sep=";",
    decimal=",",
    index=False,
    encoding="utf-8-sig"

)

print("\n✓ model_metrics.csv exported")

print(metrics)

# ==========================================================
# EXPORT 2 - ML PREDICTIONS
# ==========================================================

predictions = pd.DataFrame({

    "Claim_ID": claim_test.values,

    "Actual": y_test.values,

    "Prediction": pred,

    "Fraud_Probability": prob

})

predictions.to_csv(

    os.path.join(
        OUTPUT_FOLDER,
        "ml_predictions.csv"
    ),

    index=False

)

print("✓ ml_predictions.csv exported")

# ==========================================================
# EXPORT 3 - CONFUSION MATRIX
# ==========================================================

cm = confusion_matrix(y_test, pred)

cm_df = pd.DataFrame(

    cm,

    columns=[
        "Predicted_No_Fraud",
        "Predicted_Fraud"
    ],

    index=[
        "Actual_No_Fraud",
        "Actual_Fraud"
    ]

)

cm_df.to_csv(

    os.path.join(
        OUTPUT_FOLDER,
        "confusion_matrix.csv"
    )

)

print("✓ confusion_matrix.csv exported")

# ==========================================================
# EXPORT 4 - ROC CURVE
# ==========================================================

fpr, tpr, thresholds = roc_curve(y_test, prob)

roc_df = pd.DataFrame({

    "False_Positive_Rate": fpr,

    "True_Positive_Rate": tpr,

    "Threshold": thresholds

})

roc_df.to_csv(

    os.path.join(
        OUTPUT_FOLDER,
        "roc_curve.csv"
    ),

    index=False

)

print("✓ roc_curve.csv exported")

# ==========================================================
# EXPORT 5 - FEATURE IMPORTANCE
# ==========================================================

if hasattr(best_model, "feature_importances_"):

    feature_importance = pd.DataFrame({

        "Feature": X_train.columns,

        "Importance": best_model.feature_importances_

    })

    feature_importance = feature_importance.sort_values(

        "Importance",

        ascending=False

    )

    feature_importance.to_csv(

        os.path.join(
            OUTPUT_FOLDER,
            "feature_importance.csv"
        ),

        index=False

    )

    print("✓ feature_importance.csv exported")

else:

    print("Feature importance not available for this model.")

# ==========================================================
# EXPORT 6 - HIGH RISK CLAIMS
# ==========================================================

high_risk_claims = predictions.sort_values(

    "Fraud_Probability",

    ascending=False

).head(100)

high_risk_claims.to_csv(

    os.path.join(
        OUTPUT_FOLDER,
        "high_risk_claims.csv"
    ),

    index=False

)

print("✓ high_risk_claims.csv exported")

# ==========================================================
# EXPORT SHAP VALUES
# ==========================================================

import shap

print("\nCalculating SHAP values...")

explainer = shap.Explainer(best_model, X_train)

shap_values = explainer(X_test)

values = np.abs(shap_values.values)

# SHAP para clasificación puede devolver 3 dimensiones
if values.ndim == 3:
    values = values[:, :, 1]

mean_shap = values.mean(axis=0)

feature_names = X_train.columns

shap_df = pd.DataFrame({

    "Feature": feature_names,

    "Mean_SHAP": mean_shap

})

shap_df = shap_df.sort_values(

    "Mean_SHAP",

    ascending=False

)

shap_df.to_csv(

    os.path.join(
        OUTPUT_FOLDER,
        "shap_values.csv"
    ),

    index=False

)

print("✓ shap_values.csv exported")