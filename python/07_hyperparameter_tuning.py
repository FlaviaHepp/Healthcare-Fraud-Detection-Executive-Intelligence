# ==========================================================
# BLOQUE 9 - HYPERPARAMETER OPTIMIZATION
# ==========================================================

# ==========================================================
# IMPORTACIONES
# ==========================================================

import pandas as pd
import numpy as np

from sklearn.model_selection import (
    train_test_split,
    RandomizedSearchCV
)

from sklearn.preprocessing import (
    LabelEncoder,
    StandardScaler
)

from sklearn.impute import SimpleImputer

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier

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
# LABEL ENCODER
# ==========================================================

encoders = {}

categorical_cols = model_df.select_dtypes(
    include=["object", "category"]
).columns

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

X_train_scaled = pd.DataFrame(
    scaler.fit_transform(X_train),
    columns=X_train.columns
)

X_test_scaled = pd.DataFrame(
    scaler.transform(X_test),
    columns=X_test.columns
)

# ==========================================================
# ELEGIR EL MODELO A OPTIMIZAR
# ==========================================================

# Cambia este valor por el modelo que obtuvo el mejor ROC AUC
best_model_name = "Random Forest"

print(f"\nOptimizing: {best_model_name}")

print("=" * 80)
print("HYPERPARAMETER OPTIMIZATION")
print("=" * 80)

from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

# ==========================================================
# Seleccionar el mejor modelo
# ==========================================================

# Escribe aquí el modelo que quieras optimizar
best_model_name = "Random Forest"

# O usa alguno de estos:
# best_model_name = "XGBoost"
# best_model_name = "LightGBM"
# best_model_name = "CatBoost"
# best_model_name = "Logistic Regression"

print(f"\nOptimizing: {best_model_name}")

# ==========================================================
# Configuración según el modelo
# ==========================================================

if best_model_name == "Random Forest":

    estimator = RandomForestClassifier(random_state=42)

    param_grid = {
        "n_estimators": [200,300,400,500],
        "max_depth": [5,10,15,20,None],
        "min_samples_split": [2,5,10],
        "min_samples_leaf": [1,2,4],
        "max_features": ["sqrt","log2"]
    }

    Xtr = X_train
    Xte = X_test

elif best_model_name == "XGBoost":

    estimator = XGBClassifier(
        random_state=42,
        eval_metric="logloss"
    )

    param_grid = {
        "n_estimators":[200,300,400],
        "max_depth":[3,5,7,9],
        "learning_rate":[0.01,0.05,0.1],
        "subsample":[0.8,0.9,1],
        "colsample_bytree":[0.8,0.9,1]
    }

    Xtr = X_train
    Xte = X_test

elif best_model_name == "LightGBM":

    estimator = LGBMClassifier(random_state=42)

    param_grid = {
        "n_estimators":[200,300,400],
        "learning_rate":[0.01,0.05,0.1],
        "num_leaves":[20,31,50],
        "max_depth":[5,10,-1]
    }

    Xtr = X_train
    Xte = X_test

elif best_model_name == "CatBoost":

    estimator = CatBoostClassifier(
        verbose=False,
        random_state=42
    )

    param_grid = {
        "iterations":[200,300,500],
        "depth":[4,6,8],
        "learning_rate":[0.01,0.05,0.1]
    }

    Xtr = X_train
    Xte = X_test

else:

    estimator = LogisticRegression(max_iter=1000)

    param_grid = {
        "C":[0.01,0.1,1,10],
        "penalty":["l2"]
    }

    Xtr = X_train_scaled
    Xte = X_test_scaled

# ==========================================================
# Random Search
# ==========================================================

search = RandomizedSearchCV(

    estimator=estimator,

    param_distributions=param_grid,

    n_iter=20,

    scoring="roc_auc",

    cv=5,

    random_state=42,

    n_jobs=-1

)

search.fit(Xtr, y_train)

# ==========================================================
# Mejor modelo
# ==========================================================

best_model = search.best_estimator_

import joblib

joblib.dump(best_model, "best_healthcare_fraud_model.pkl")

print("Best model saved successfully.")

print("\nBest Parameters\n")

print(search.best_params_)

# ==========================================================
# Evaluación
# ==========================================================

pred = best_model.predict(Xte)

prob = best_model.predict_proba(Xte)[:,1]

results_optimized = pd.DataFrame({

    "Metric":[
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "ROC AUC"
    ],

    "Value":[

        accuracy_score(y_test,pred),

        precision_score(y_test,pred),

        recall_score(y_test,pred),

        f1_score(y_test,pred),

        roc_auc_score(y_test,prob)

    ]

})

print(results_optimized)