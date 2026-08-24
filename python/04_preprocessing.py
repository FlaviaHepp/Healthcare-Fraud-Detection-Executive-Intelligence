# ==========================================================
# BLOQUE 6 - DATA PREPROCESSING
# ==========================================================

# ==========================================================
# IMPORTACIÓN DE LIBRERÍAS
# ==========================================================

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("dark_background")

sns.set_theme(
    style="darkgrid",
    palette="viridis"
)

pd.set_option("display.max_columns", None)

# ==========================================================
# CARGA DEL DATASET
# ==========================================================

DATA_PATH = "healthcare_fraud_detection.csv"

df = pd.read_csv(DATA_PATH)

print("=" * 80)
print("DATA PREPROCESSING")
print("=" * 80)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# ==========================================================
# Copia del dataset
# ==========================================================

model_df = df.copy()

# ==========================================================
# Eliminar columnas que NO deben utilizarse
# ==========================================================

columns_to_drop = [

    "Claim_ID",
    "Patient_ID",
    "Provider_ID",

    "Claim_Submission_Date",
    "Service_Date",

    # Evitar Data Leakage
    "Provider_Historical_Fraud_Rate"

]

for col in columns_to_drop:
    if col in model_df.columns:
        model_df.drop(columns=col, inplace=True)

print("\nColumnas eliminadas:")
print(columns_to_drop)

# ==========================================================
# Codificación de variables categóricas
# ==========================================================

categorical_cols = model_df.select_dtypes(include=["object","category"]).columns

encoders = {}

for col in categorical_cols:

    encoder = LabelEncoder()

    model_df[col] = encoder.fit_transform(
        model_df[col].astype(str)
    )

    encoders[col] = encoder

print(f"\nVariables categóricas codificadas: {len(categorical_cols)}")

# ==========================================================
# Separar X e y
# ==========================================================

X = model_df.drop("Is_Fraud", axis=1)

y = model_df["Is_Fraud"]

print("\nShape de X:", X.shape)
print("Shape de y:", y.shape)

# ==========================================================
# División Train/Test
# ==========================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.20,

    random_state=42,

    stratify=y

)

print("\nTrain Shape:", X_train.shape)
print("Test Shape :", X_test.shape)

# ==========================================================
# Escalado
# ==========================================================

numeric_columns = X_train.select_dtypes(include="number").columns

scaler = StandardScaler()

X_train_scaled = X_train.copy()
X_test_scaled = X_test.copy()

X_train_scaled[numeric_columns] = scaler.fit_transform(
    X_train[numeric_columns]
)

X_test_scaled[numeric_columns] = scaler.transform(
    X_test[numeric_columns]
)

print("\nEscalado realizado correctamente.")

# ==========================================================
# Balance de clases
# ==========================================================

print("\nDistribución de clases")

print(y.value_counts())

print("\nPorcentaje")

print(round(y.value_counts(normalize=True)*100,2))

# ==========================================================
# Resumen final
# ==========================================================

print("\n")
print("=" * 80)
print("DATASET READY FOR MACHINE LEARNING")
print("=" * 80)

print(f"Variables Predictoras : {X.shape[1]}")
print(f"Observaciones         : {X.shape[0]}")
print(f"Train                 : {X_train.shape[0]}")
print(f"Test                  : {X_test.shape[0]}")