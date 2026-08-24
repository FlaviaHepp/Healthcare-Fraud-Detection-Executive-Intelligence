# ==========================================================
# BLOQUE 7 - MACHINE LEARNING BENCHMARK
# ==========================================================

# ==========================================================
# IMPORTACIONES NECESARIAS (TEMPORAL)
# ==========================================================

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

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
        if col in model_df.columns:
            model_df.drop(columns=col, inplace=True)
            


# ==========================================================
# CODIFICAR VARIABLES CATEGÓRICAS
# ==========================================================

categorical_cols = model_df.select_dtypes(include=["object", "category"]).columns

encoder = LabelEncoder()

for col in categorical_cols:
    model_df[col] = encoder.fit_transform(model_df[col].astype(str))

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
# ESCALADO
# ==========================================================

numeric_columns = X_train.select_dtypes(include=np.number).columns

scaler = StandardScaler()

X_train_scaled = X_train.copy()
X_test_scaled = X_test.copy()

X_train_scaled[numeric_columns] = scaler.fit_transform(X_train[numeric_columns])
X_test_scaled[numeric_columns] = scaler.transform(X_test[numeric_columns])

print("=" * 80)
print("MODEL TRAINING")
print("=" * 80)

import time

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

# ==========================================================
# TRATAMIENTO DE VALORES NULOS
# ==========================================================

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy="median")

X_train = pd.DataFrame(
    imputer.fit_transform(X_train),
    columns=X_train.columns
)

X_test = pd.DataFrame(
    imputer.transform(X_test),
    columns=X_test.columns
)

X_train_scaled = pd.DataFrame(
    imputer.fit_transform(X_train_scaled),
    columns=X_train_scaled.columns
)

X_test_scaled = pd.DataFrame(
    imputer.transform(X_test_scaled),
    columns=X_test_scaled.columns
)

from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier

# ==========================================================
# Modelos
# ==========================================================

models = {

    "Logistic Regression": (
        LogisticRegression(max_iter=1000),
        X_train_scaled,
        X_test_scaled
    ),

    "Random Forest": (
        RandomForestClassifier(
            n_estimators=300,
            random_state=42
        ),
        X_train,
        X_test
    ),

    "XGBoost": (
        XGBClassifier(
            random_state=42,
            eval_metric="logloss"
        ),
        X_train,
        X_test
    ),

    "LightGBM": (
        LGBMClassifier(
            random_state=42
        ),
        X_train,
        X_test
    ),

    "CatBoost": (
        CatBoostClassifier(
            verbose=False,
            random_state=42
        ),
        X_train,
        X_test
    )

}

results = []

# ==========================================================
# Entrenamiento
# ==========================================================

for name, (model, Xtr, Xte) in models.items():

    print(f"\nTraining {name}...")

    start = time.time()

    model.fit(Xtr, y_train)

    elapsed = time.time() - start

    predictions = model.predict(Xte)

    probabilities = model.predict_proba(Xte)[:,1]

    results.append({

        "Model": name,

        "Accuracy": accuracy_score(
            y_test,
            predictions
        ),

        "Precision": precision_score(
            y_test,
            predictions
        ),

        "Recall": recall_score(
            y_test,
            predictions
        ),

        "F1-Score": f1_score(
            y_test,
            predictions
        ),

        "ROC AUC": roc_auc_score(
            y_test,
            probabilities
        ),

        "Training Time (s)": elapsed

    })

# ==========================================================
# Resultados
# ==========================================================

results_df = (
    pd.DataFrame(results)
    .sort_values(
        "ROC AUC",
        ascending=False
    )
)

print(results_df)

print("\n")
print("="*80)
print("BEST MODEL")
print("="*80)

print(results_df.head(1))