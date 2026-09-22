"""
Build the final machine-learning artifact for:

Healthcare Fraud Detection & Executive Intelligence

What this script does:
1. Loads healthcare_fraud_detection.csv from data/raw/
2. Cleans/prepares the modeling dataset
3. Trains several fraud-classification models
4. Compares them using standard classification metrics
5. Selects the model with the highest ROC-AUC on the held-out test set
6. Saves ONLY the final/best model as:
      models/best_healthcare_fraud_model.pkl
7. Saves model comparison results as:
      results/model_metrics.csv
8. Saves model metadata as:
      models/model_metadata.json

IMPORTANT:
This script does NOT create fake models. The .pkl file is generated
from the real dataset in your project.
"""

from __future__ import annotations

import json
import sys
import warnings
from datetime import datetime
from pathlib import Path

warnings.filterwarnings("ignore")

import joblib
import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler


# ============================================================
# OPTIONAL ML LIBRARIES
# ============================================================

try:
    from xgboost import XGBClassifier

    XGBOOST_AVAILABLE = True
    XGBOOST_ERROR = ""
except Exception as exc:
    XGBClassifier = None
    XGBOOST_AVAILABLE = False
    XGBOOST_ERROR = str(exc)

try:
    from lightgbm import LGBMClassifier

    LIGHTGBM_AVAILABLE = True
    LIGHTGBM_ERROR = ""
except Exception as exc:
    LGBMClassifier = None
    LIGHTGBM_AVAILABLE = False
    LIGHTGBM_ERROR = str(exc)

try:
    from catboost import CatBoostClassifier

    CATBOOST_AVAILABLE = True
    CATBOOST_ERROR = ""
except Exception as exc:
    CatBoostClassifier = None
    CATBOOST_AVAILABLE = False
    CATBOOST_ERROR = str(exc)


# ============================================================
# PROJECT PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent

DATA_PATH = PROJECT_ROOT / "data" / "raw" / "healthcare_fraud_detection.csv"
MODELS_DIR = PROJECT_ROOT / "models"
RESULTS_DIR = PROJECT_ROOT / "results"

BEST_MODEL_PATH = MODELS_DIR / "best_healthcare_fraud_model.pkl"
METRICS_PATH = RESULTS_DIR / "model_metrics.csv"
METADATA_PATH = MODELS_DIR / "model_metadata.json"


# ============================================================
# SETTINGS
# ============================================================

TARGET = "Is_Fraud"
TEST_SIZE = 0.20
RANDOM_STATE = 42


# ============================================================
# HELPERS
# ============================================================

def print_header(title: str) -> None:
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def fail(message: str) -> None:
    print("\nERROR:")
    print(message)
    sys.exit(1)


# ============================================================
# 1. LOAD DATA
# ============================================================

def load_data() -> pd.DataFrame:
    print_header("1. LOADING DATA")

    if not DATA_PATH.exists():
        fail(
            f"Dataset not found:\n\n"
            f"{DATA_PATH}\n\n"
            "Put your file here:\n"
            "data/raw/healthcare_fraud_detection.csv"
        )

    df = pd.read_csv(DATA_PATH)

    # Remove accidental spaces from column names.
    df.columns = df.columns.astype(str).str.strip()

    print(f"Dataset path: {DATA_PATH}")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    if TARGET not in df.columns:
        fail(
            f"The target column '{TARGET}' was not found.\n\n"
            f"Available columns:\n{df.columns.tolist()}"
        )

    if df[TARGET].isna().any():
        fail(
            f"The target column '{TARGET}' contains missing values. "
            "Clean the target before training."
        )

    unique_target_values = df[TARGET].dropna().unique()

    if len(unique_target_values) != 2:
        fail(
            f"'{TARGET}' must contain exactly two classes for binary "
            f"classification. Found: {unique_target_values}"
        )

    print("\nTarget distribution:")
    print(df[TARGET].value_counts(dropna=False))

    return df


# ============================================================
# 2. PREPARE DATA
# ============================================================

def prepare_data(df: pd.DataFrame):
    print_header("2. PREPARING MODEL DATA")

    model_df = df.copy()

    # Preserve Claim_ID for later interpretation/output.
    if "Claim_ID" in model_df.columns:
        claim_ids = model_df["Claim_ID"].copy()
    else:
        claim_ids = pd.Series(
            np.arange(len(model_df)),
            name="Claim_ID",
        )

    # These are identifiers / leakage-prone fields / dates that
    # are intentionally removed according to the project's
    # existing export workflow.
    columns_to_drop = [
        "Claim_ID",
        "Patient_ID",
        "Provider_ID",
        "Claim_Submission_Date",
        "Service_Date",
        "Provider_Historical_Fraud_Rate",
    ]

    existing_drops = [
        col for col in columns_to_drop if col in model_df.columns
    ]

    model_df.drop(
        columns=existing_drops,
        inplace=True,
        errors="ignore",
    )

    y = model_df[TARGET].copy()
    X = model_df.drop(columns=[TARGET]).copy()

    # Encode categorical variables.
    categorical_cols = X.select_dtypes(
        include=["object", "category", "string"]
    ).columns.tolist()

    encoders: dict[str, LabelEncoder] = {}

    for col in categorical_cols:
        encoder = LabelEncoder()

        X[col] = encoder.fit_transform(
            X[col].astype(str)
        )

        encoders[col] = encoder

    # Convert everything else to numeric where possible.
    X = X.apply(pd.to_numeric, errors="coerce")

    feature_columns = X.columns.tolist()

    print(f"Removed columns: {existing_drops}")
    print(f"Categorical variables encoded: {len(categorical_cols)}")
    print(f"Model features: {len(feature_columns)}")

    return (
        claim_ids,
        X,
        y,
        categorical_cols,
        encoders,
        existing_drops,
        feature_columns,
    )


# ============================================================
# 3. BUILD MODELS
# ============================================================

def build_models(y_train: pd.Series):
    print_header("3. BUILDING MODELS")

    fraud_count = int((y_train == 1).sum())
    non_fraud_count = int((y_train == 0).sum())

    if fraud_count == 0:
        scale_pos_weight = 1.0
    else:
        scale_pos_weight = non_fraud_count / fraud_count

    models = {
        "Logistic Regression": LogisticRegression(
            max_iter=2000,
            class_weight="balanced",
            random_state=RANDOM_STATE,
        ),

        "Random Forest": RandomForestClassifier(
            n_estimators=300,
            random_state=RANDOM_STATE,
            n_jobs=-1,
            class_weight="balanced",
        ),
    }

    if XGBOOST_AVAILABLE:
        models["XGBoost"] = XGBClassifier(
            n_estimators=300,
            max_depth=6,
            learning_rate=0.05,
            subsample=0.80,
            colsample_bytree=0.80,
            objective="binary:logistic",
            eval_metric="logloss",
            scale_pos_weight=scale_pos_weight,
            random_state=RANDOM_STATE,
            n_jobs=-1,
        )
    else:
        print(f"⚠ XGBoost unavailable: {XGBOOST_ERROR}")

    if LIGHTGBM_AVAILABLE:
        models["LightGBM"] = LGBMClassifier(
            n_estimators=300,
            learning_rate=0.05,
            num_leaves=31,
            subsample=0.80,
            colsample_bytree=0.80,
            objective="binary",
            random_state=RANDOM_STATE,
            n_jobs=-1,
            verbosity=-1,
        )
    else:
        print(f"⚠ LightGBM unavailable: {LIGHTGBM_ERROR}")

    if CATBOOST_AVAILABLE:
        models["CatBoost"] = CatBoostClassifier(
            iterations=300,
            depth=6,
            learning_rate=0.05,
            loss_function="Logloss",
            eval_metric="AUC",
            random_seed=RANDOM_STATE,
            verbose=False,
            thread_count=-1,
        )
    else:
        print(f"⚠ CatBoost unavailable: {CATBOOST_ERROR}")

    print("\nModels available:")
    for name in models:
        print(f" - {name}")

    return models


# ============================================================
# 4. EVALUATION
# ============================================================

def evaluate_model(model, X_eval, y_eval) -> dict:
    predictions = model.predict(X_eval)
    probabilities = model.predict_proba(X_eval)[:, 1]

    return {
        "Accuracy": accuracy_score(
            y_eval,
            predictions,
        ),
        "Precision": precision_score(
            y_eval,
            predictions,
            zero_division=0,
        ),
        "Recall": recall_score(
            y_eval,
            predictions,
            zero_division=0,
        ),
        "F1": f1_score(
            y_eval,
            predictions,
            zero_division=0,
        ),
        "ROC_AUC": roc_auc_score(
            y_eval,
            probabilities,
        ),
    }


# ============================================================
# 5. TRAIN / COMPARE / SELECT
# ============================================================

def train_and_compare(
    models,
    X_train_imp,
    X_test_imp,
    X_train_scaled,
    X_test_scaled,
    y_train,
    y_test,
):
    print_header("4. TRAINING & MODEL BENCHMARKING")

    metrics_rows = []
    fitted_models = {}

    for name, model in models.items():

        print(f"\nTraining: {name}")

        # Logistic Regression uses scaled features.
        if name == "Logistic Regression":
            X_fit = X_train_scaled
            X_eval = X_test_scaled
        else:
            # Tree-based models can use imputed, unscaled features.
            X_fit = X_train_imp
            X_eval = X_test_imp

        model.fit(X_fit, y_train)

        metrics = evaluate_model(
            model,
            X_eval,
            y_test,
        )

        metrics["Model"] = name

        metrics_rows.append(metrics)
        fitted_models[name] = model

        print(
            f"Accuracy={metrics['Accuracy']:.4f} | "
            f"Precision={metrics['Precision']:.4f} | "
            f"Recall={metrics['Recall']:.4f} | "
            f"F1={metrics['F1']:.4f} | "
            f"ROC-AUC={metrics['ROC_AUC']:.4f}"
        )

    metrics_df = pd.DataFrame(metrics_rows)

    metrics_df = metrics_df[
        [
            "Model",
            "Accuracy",
            "Precision",
            "Recall",
            "F1",
            "ROC_AUC",
        ]
    ].sort_values(
        by="ROC_AUC",
        ascending=False,
    )

    return metrics_df, fitted_models


# ============================================================
# 6. SAVE FINAL MODEL
# ============================================================

def save_final_model(
    metrics_df: pd.DataFrame,
    fitted_models: dict,
    feature_columns: list[str],
    categorical_cols: list[str],
    columns_to_drop: list[str],
):
    print_header("5. SAVING FINAL MODEL")

    best_model_name = metrics_df.iloc[0]["Model"]
    best_model = fitted_models[best_model_name]

    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    # Save ONLY the selected final model.
    joblib.dump(
        best_model,
        BEST_MODEL_PATH,
    )

    print(f"✓ Best model: {best_model_name}")
    print(f"✓ Saved: {BEST_MODEL_PATH}")

    # Save benchmark results.
    metrics_df.to_csv(
        METRICS_PATH,
        index=False,
    )

    print(f"✓ Saved: {METRICS_PATH}")

    metadata = {
        "created_at": datetime.utcnow().isoformat() + "Z",
        "target": TARGET,
        "best_model": best_model_name,
        "selection_metric": "ROC_AUC",
        "test_size": TEST_SIZE,
        "random_state": RANDOM_STATE,
        "feature_count": len(feature_columns),
        "features": feature_columns,
        "categorical_features": categorical_cols,
        "dropped_columns": columns_to_drop,
        "available_models": metrics_df["Model"].tolist(),
    }

    METADATA_PATH.write_text(
        json.dumps(
            metadata,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(f"✓ Saved: {METADATA_PATH}")

    return best_model_name


# ============================================================
# 7. MAIN
# ============================================================

def main():
    print_header(
        "HEALTHCARE FRAUD DETECTION — MODEL ARTIFACT BUILDER"
    )

    print("Python:", sys.version.split()[0])
    print("Project root:", PROJECT_ROOT)

    # Create folders if necessary.
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    # Load.
    df = load_data()

    # Prepare.
    (
        claim_ids,
        X,
        y,
        categorical_cols,
        encoders,
        columns_to_drop,
        feature_columns,
    ) = prepare_data(df)

    # Split.
    (
        X_train,
        X_test,
        y_train,
        y_test,
        claim_train,
        claim_test,
    ) = train_test_split(
        X,
        y,
        claim_ids,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y,
    )

    print_header("TRAIN / TEST SPLIT")

    print("Training rows:", len(X_train))
    print("Test rows:    ", len(X_test))

    # Imputation.
    imputer = SimpleImputer(
        strategy="median"
    )

    X_train_imp = pd.DataFrame(
        imputer.fit_transform(X_train),
        columns=feature_columns,
        index=X_train.index,
    )

    X_test_imp = pd.DataFrame(
        imputer.transform(X_test),
        columns=feature_columns,
        index=X_test.index,
    )

    # Scaling for Logistic Regression.
    scaler = StandardScaler()

    X_train_scaled = X_train_imp.copy()
    X_test_scaled = X_test_imp.copy()

    X_train_scaled[feature_columns] = scaler.fit_transform(
        X_train_imp
    )

    X_test_scaled[feature_columns] = scaler.transform(
        X_test_imp
    )

    models = build_models(y_train)

    metrics_df, fitted_models = train_and_compare(
        models=models,
        X_train_imp=X_train_imp,
        X_test_imp=X_test_imp,
        X_train_scaled=X_train_scaled,
        X_test_scaled=X_test_scaled,
        y_train=y_train,
        y_test=y_test,
    )

    print_header("MODEL COMPARISON")

    print(
        metrics_df.to_string(
            index=False,
            float_format=lambda value: f"{value:.4f}",
        )
    )

    best_model_name = save_final_model(
        metrics_df=metrics_df,
        fitted_models=fitted_models,
        feature_columns=feature_columns,
        categorical_cols=categorical_cols,
        columns_to_drop=columns_to_drop,
    )

    print_header("COMPLETE")

    print(
        "\nThe project now has the ONE model artifact needed "
        "by the existing prediction/export workflow:"
    )

    print(f"\n  {BEST_MODEL_PATH}")

    print(
        "\nOptional comparison and documentation files:"
    )

    print(f"  {METRICS_PATH}")
    print(f"  {METADATA_PATH}")

    print(
        "\nNext step:"
        "\nRun your export-results script and verify that it loads"
        "\nbest_healthcare_fraud_model.pkl successfully."
    )

    print(
        f"\nSelected model: {best_model_name}"
    )


if __name__ == "__main__":
    main()
