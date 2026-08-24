# ==========================================================
# BLOQUE 1 - CONFIGURACIÓN E IMPORTACIÓN DEL DATASET
# Healthcare Fraud Detection AI Platform
# ==========================================================

# ==========================
# Librerías
# ==========================

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from pathlib import Path

# ==========================================================
# Configuración de gráficos
# ==========================================================

plt.style.use("dark_background")

sns.set_theme(
    style="darkgrid",
    palette="viridis"
)

plt.rcParams["figure.figsize"] = (12,6)
plt.rcParams["axes.facecolor"] = "#111111"
plt.rcParams["figure.facecolor"] = "#111111"
plt.rcParams["savefig.facecolor"] = "#111111"

# ==========================================================
# Configuración de pandas
# ==========================================================

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)
pd.set_option("display.max_colwidth", None)

# ==========================================================
# Cargar dataset
# ==========================================================

DATA_PATH = "healthcare_fraud_detection.csv"

df = pd.read_csv(DATA_PATH)

# ==========================================================
# Información general
# ==========================================================

print("="*70)
print("HEALTHCARE FRAUD DETECTION DATASET")
print("="*70)

print(f"\nFilas: {df.shape[0]:,}")
print(f"Columnas: {df.shape[1]}")

print("\nColumnas:")

for col in df.columns:
    print(f"• {col}")

print("\nPrimeras filas")

print(df.head())

print("\nInformación del dataset")

print(df.info())

print("\nEstadísticas descriptivas")

print(df.describe(include="all").T)

# ==========================================================
# BLOQUE 2 - DATA QUALITY ASSESSMENT
# ==========================================================

print("=" * 80)
print("DATA QUALITY REPORT")
print("=" * 80)

# ==========================================================
# Dimensiones del dataset
# ==========================================================

print(f"\nDataset Shape: {df.shape[0]:,} filas x {df.shape[1]} columnas")

# ==========================================================
# Tipos de datos
# ==========================================================

print("\nTipos de datos:\n")
print(df.dtypes.to_frame(name="Data Type"))

# ==========================================================
# Valores nulos
# ==========================================================

missing = pd.DataFrame({
    "Missing Values": df.isnull().sum(),
    "Percentage (%)": round(df.isnull().mean() * 100, 2)
}).sort_values("Missing Values", ascending=False)

print(missing)

# ==========================================================
# Valores duplicados
# ==========================================================

duplicates = df.duplicated().sum()

print(f"\nDuplicated Rows: {duplicates:,}")

# ==========================================================
# Valores únicos
# ==========================================================

unique_values = pd.DataFrame({
    "Unique Values": df.nunique(),
    "Data Type": df.dtypes
}).sort_values("Unique Values")

print(unique_values)

# ==========================================================
# Uso de memoria
# ==========================================================

memory = df.memory_usage(deep=True).sum() / 1024**2

print(f"\nMemory Usage: {memory:.2f} MB")

# ==========================================================
# Columnas constantes
# ==========================================================

constant_columns = [
    col for col in df.columns
    if df[col].nunique() == 1
]

print("\nConstant Columns:")

if constant_columns:
    for col in constant_columns:
        print(f"• {col}")
else:
    print("None")

# ==========================================================
# Variables categóricas y numéricas
# ==========================================================

categorical_cols = df.select_dtypes(include=["object"]).columns.tolist()

numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

print(f"\nCategorical Variables ({len(categorical_cols)}):")
print(categorical_cols)

print(f"\nNumeric Variables ({len(numeric_cols)}):")
print(numeric_cols)

# ==========================================================
# Resumen Ejecutivo
# ==========================================================

summary = pd.DataFrame({
    "Metric": [
        "Rows",
        "Columns",
        "Numeric Variables",
        "Categorical Variables",
        "Duplicate Rows",
        "Missing Values",
        "Memory (MB)"
    ],
    "Value": [
        df.shape[0],
        df.shape[1],
        len(numeric_cols),
        len(categorical_cols),
        duplicates,
        int(df.isnull().sum().sum()),
        round(memory,2)
    ]
})

print("\nExecutive Summary\n")

print(summary)