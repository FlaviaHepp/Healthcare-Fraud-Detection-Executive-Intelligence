# ==========================================================
# BLOQUE 5 - FEATURE ENGINEERING
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
print("FEATURE ENGINEERING")
print("=" * 80)

# Crear una copia para trabajar
df_fe = df.copy()

# ==========================================================
# Convertir fechas
# ==========================================================

date_columns = [
    "Claim_Submission_Date",
    "Service_Date"
]

for col in date_columns:
    if col in df_fe.columns:
        df_fe[col] = pd.to_datetime(df_fe[col])

# ==========================================================
# Variables temporales
# ==========================================================

df_fe["Claim_Year"] = df_fe["Claim_Submission_Date"].dt.year
df_fe["Claim_Month"] = df_fe["Claim_Submission_Date"].dt.month
df_fe["Claim_Day"] = df_fe["Claim_Submission_Date"].dt.day
df_fe["Claim_Weekday"] = df_fe["Claim_Submission_Date"].dt.day_name()

# ==========================================================
# Diferencia entre reclamado y aprobado
# ==========================================================

df_fe["Claim_Approval_Difference"] = (
    df_fe["Claim_Amount"] -
    df_fe["Approved_Amount"]
)

# ==========================================================
# Porcentaje aprobado
# ==========================================================

df_fe["Approval_Rate"] = (
    df_fe["Approved_Amount"] /
    df_fe["Claim_Amount"]
)

# Evitar infinitos
df_fe["Approval_Rate"] = df_fe["Approval_Rate"].replace(
    [np.inf, -np.inf],
    np.nan
)

# ==========================================================
# Pacientes de edad avanzada
# ==========================================================

df_fe["Senior_Patient"] = np.where(
    df_fe["Patient_Age"] >= 65,
    1,
    0
)

# ==========================================================
# Hospitalización prolongada
# ==========================================================

df_fe["Long_Stay"] = np.where(
    df_fe["Length_of_Stay"] >= 7,
    1,
    0
)

# ==========================================================
# Alta frecuencia de visitas
# ==========================================================

threshold = df_fe["Prior_Visits_12m"].quantile(0.75)

df_fe["High_Visit_Frequency"] = np.where(
    df_fe["Prior_Visits_12m"] >= threshold,
    1,
    0
)

# ==========================================================
# Monto reclamado alto
# ==========================================================

claim_threshold = df_fe["Claim_Amount"].quantile(0.90)

df_fe["High_Claim"] = np.where(
    df_fe["Claim_Amount"] >= claim_threshold,
    1,
    0
)

# ==========================================================
# Ratio días de espera
# ==========================================================

df_fe["Delay_Category"] = pd.cut(
    df_fe["Days_Between_Service_and_Claim"],
    bins=[-1,7,30,90,1000],
    labels=[
        "Very Fast",
        "Fast",
        "Delayed",
        "Very Delayed"
    ]
)

# ==========================================================
# Provider Claim Count
# ==========================================================

provider_claims = (
    df_fe.groupby("Provider_ID")
         .size()
)

df_fe["Provider_Claim_Count"] = (
    df_fe["Provider_ID"]
        .map(provider_claims)
)

# ==========================================================
# Average Claim by Provider
# ==========================================================

provider_avg = (
    df_fe.groupby("Provider_ID")["Claim_Amount"]
         .mean()
)

df_fe["Provider_Avg_Claim"] = (
    df_fe["Provider_ID"]
        .map(provider_avg)
)

# ==========================================================
# Average Fraud Rate by Provider
# ==========================================================

provider_fraud = (
    df_fe.groupby("Provider_ID")["Is_Fraud"]
         .mean()
)

df_fe["Provider_Historical_Fraud_Rate"] = (
    df_fe["Provider_ID"]
        .map(provider_fraud)
)

# ==========================================================
# Revisar nuevas variables
# ==========================================================

print("\nNuevas variables creadas:\n")

new_features = [
    col for col in df_fe.columns
    if col not in df.columns
]

for feature in new_features:
    print("✔", feature)

print("\nTotal nuevas variables:", len(new_features))

print(df_fe.head())