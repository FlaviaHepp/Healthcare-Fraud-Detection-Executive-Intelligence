# ==========================================================
# IMPORTACIONES
# ==========================================================

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier

# ==========================================================
# CARGAR DATASET
# ==========================================================

df = pd.read_csv("healthcare_fraud_detection.csv")

model_df = df.copy()

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

categorical_cols = model_df.select_dtypes(
    include=["object", "category"]
).columns

for col in categorical_cols:

    encoder = LabelEncoder()

    model_df[col] = encoder.fit_transform(
        model_df[col].astype(str)
    )

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
# ENTRENAR EL MODELO
# ==========================================================

best_model_name = "Random Forest"

best_model = RandomForestClassifier(
    n_estimators=300,
    random_state=42
)

best_model.fit(X_train, y_train)

X_eval = X_test