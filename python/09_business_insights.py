# ==========================================================
# BLOQUE 11 - BUSINESS INTELLIGENCE & EXECUTIVE INSIGHTS
# ==========================================================

# ==========================================================
# IMPORTACIONES
# ==========================================================

import pandas as pd
import numpy as np

# ==========================================================
# CARGAR DATASET
# ==========================================================

df = pd.read_csv("healthcare_fraud_detection.csv")

# ==========================================================
# LIMPIEZA BÁSICA (opcional)
# ==========================================================

# Eliminar filas completamente vacías
df.dropna(how="all", inplace=True)

# Eliminar duplicados
df.drop_duplicates(inplace=True)

# Convertir columnas numéricas si fueran texto
numeric_columns = [
    "Claim_Amount",
    "Approved_Amount",
    "Patient_Age",
    "Length_of_Stay",
    "Days_Between_Service_and_Claim"
]

for col in numeric_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Reemplazar valores faltantes en columnas numéricas
df[numeric_columns] = df[numeric_columns].fillna(
    df[numeric_columns].median(numeric_only=True)
)

print("Dataset cargado correctamente.")
print(f"Registros: {len(df):,}")
print(f"Columnas : {len(df.columns)}")

print("=" * 80)
print("BUSINESS INTELLIGENCE & EXECUTIVE INSIGHTS")
print("=" * 80)

# Trabajaremos sobre el dataset original
business_df = df.copy()

# ==========================================================
# 1. KPIs
# ==========================================================

total_claims = len(business_df)

fraud_cases = business_df["Is_Fraud"].sum()

fraud_rate = business_df["Is_Fraud"].mean() * 100

total_claim_amount = business_df["Claim_Amount"].sum()

total_approved = business_df["Approved_Amount"].sum()

estimated_loss = business_df.loc[
    business_df["Is_Fraud"] == 1,
    "Claim_Amount"
].sum()

print("\nEXECUTIVE KPIs")
print("-" * 50)

print(f"Total Claims.............: {total_claims:,}")
print(f"Fraud Cases..............: {fraud_cases:,}")
print(f"Fraud Rate...............: {fraud_rate:.2f}%")
print(f"Claim Amount............ : ${total_claim_amount:,.2f}")
print(f"Approved Amount......... : ${total_approved:,.2f}")
print(f"Potential Fraud Exposure : ${estimated_loss:,.2f}")