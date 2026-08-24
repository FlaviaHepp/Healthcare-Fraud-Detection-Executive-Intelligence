# ==========================================================
# BLOQUE 10 - EXPLAINABLE AI (SHAP + LIME)
# ==========================================================

# ==========================================================
# IMPORTACIONES
# ==========================================================

import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer

# ==========================================================
# CARGAR DATASET
# ==========================================================

df = pd.read_csv("healthcare_fraud_detection.csv")

model_df = df.copy()

# ==========================================================
# ELIMINAR COLUMNAS
# ==========================================================

columns_to_drop = [
    "Claim_ID",
    "Patient_ID",
    "Provider_ID",
    "Claim_Submission_Date",
    "Service_Date"
]

for col in columns_to_drop:
    if col in model_df.columns:
        model_df.drop(columns=col, inplace=True)

# ==========================================================
# CODIFICAR VARIABLES
# ==========================================================

categorical_cols = model_df.select_dtypes(include=["object", "category"]).columns

encoders = {}

for col in categorical_cols:

    encoder = LabelEncoder()

    model_df[col] = encoder.fit_transform(
        model_df[col].astype(str)
    )

    encoders[col] = encoder

# ==========================================================
# X e y
# ==========================================================

X = model_df.drop("Is_Fraud", axis=1)
y = model_df["Is_Fraud"]

# ==========================================================
# TRAIN TEST SPLIT
# ==========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# ==========================================================
# IMPUTACIÓN
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
# ESCALADO
# ==========================================================

scaler = StandardScaler()

X_train_scaled = X_train.copy()
X_test_scaled = X_test.copy()

X_train_scaled[X_train.columns] = scaler.fit_transform(X_train)

X_test_scaled[X_test.columns] = scaler.transform(X_test)

print("=" * 80)
print("EXPLAINABLE AI")
print("=" * 80)

import shap
import lime
import lime.lime_tabular

# ==========================================================
# Seleccionar modelo optimizado
# ==========================================================

# ==========================================================
# CARGAR MODELO ENTRENADO
# ==========================================================

import joblib

# Cargar el modelo entrenado
model = joblib.load("best_healthcare_fraud_model.pkl")

# Especificar el modelo ganador
best_model_name = "Random Forest"   # <-- Cambia este nombre por el que ganó en tu proyecto

# Seleccionar los datos adecuados
if best_model_name == "Logistic Regression":
    X_train_exp = X_train_scaled
    X_test_exp = X_test_scaled
else:
    X_train_exp = X_train
    X_test_exp = X_test

# ==========================================================
# SHAP
# ==========================================================

print("\nCalculando valores SHAP...")

explainer = shap.Explainer(model, X_train_exp)

shap_values = explainer(X_test_exp)

print("SHAP calculado correctamente.")