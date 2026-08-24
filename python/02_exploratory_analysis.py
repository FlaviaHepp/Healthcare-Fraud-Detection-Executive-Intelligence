# ==========================================================
# BLOQUE 3 - EXPLORATORY DATA ANALYSIS (EDA)
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

#sns.set_theme(
#    style="darkgrid",
#    palette="viridis"
#)

pd.set_option("display.max_columns", None)

# ==========================================================
# CARGA DEL DATASET
# ==========================================================

DATA_PATH = "healthcare_fraud_detection.csv"

df = pd.read_csv(DATA_PATH)
print("=" * 80)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 80)

# ==========================================================
# 1. Distribución de la variable objetivo
# ==========================================================

plt.figure(figsize=(8,5))

ax = sns.countplot(
    data=df,
    x="Is_Fraud",
    palette="viridis"
)

plt.title("Fraud vs Non-Fraud Claims", fontsize=16, fontweight="bold")
plt.xlabel("Fraud")
plt.ylabel("Number of Claims")

for p in ax.patches:
    ax.annotate(
        f'{int(p.get_height()):,}',
        (p.get_x() + p.get_width()/2, p.get_height()),
        ha='center',
        va='bottom',
        fontsize=11
    )

plt.show()

# ==========================================================
# 2. Distribución de edades
# ==========================================================

plt.figure(figsize=(10,5))

sns.histplot(
    df["Patient_Age"],
    bins=30,
    kde=True,
    color="cyan"
)

plt.title("Patient Age Distribution", fontsize=16, fontweight="bold")
plt.xlabel("Age")

plt.show()

# ==========================================================
# 3. Claim Amount
# ==========================================================

plt.figure(figsize=(10,5))

sns.histplot(
    df["Claim_Amount"],
    bins=40,
    kde=True,
    color="orange"
)

plt.title("Claim Amount Distribution", fontsize=16, fontweight="bold")
plt.xlabel("Claim Amount ($)")

plt.show()

# ==========================================================
# 4. Approved Amount
# ==========================================================

plt.figure(figsize=(10,5))

sns.histplot(
    df["Approved_Amount"],
    bins=40,
    kde=True,
    color="lime"
)

plt.title("Approved Amount Distribution", fontsize=16, fontweight="bold")
plt.xlabel("Approved Amount ($)")

plt.show()

# ==========================================================
# 5. Género
# ==========================================================

plt.figure(figsize=(7,5))

ax = sns.countplot(
    data=df,
    x="Patient_Gender",
    palette="magma"
)

plt.title("Patient Gender Distribution", fontsize=16, fontweight="bold")

for p in ax.patches:
    ax.annotate(
        f'{int(p.get_height()):,}',
        (p.get_x() + p.get_width()/2, p.get_height()),
        ha='center',
        va='bottom'
    )

plt.show()

# ==========================================================
# 6. Tipo de Seguro
# ==========================================================

plt.figure(figsize=(10,5))

ax = sns.countplot(
    data=df,
    x="Insurance_Type",
    palette="viridis"
)

plt.xticks(rotation=20)

plt.title("Insurance Type Distribution", fontsize=16, fontweight="bold")

for p in ax.patches:
    ax.annotate(
        f'{int(p.get_height()):,}',
        (p.get_x() + p.get_width()/2, p.get_height()),
        ha='center',
        va='bottom',
        fontsize=10
    )

plt.show()

# ==========================================================
# 7. Top 10 Estados
# ==========================================================

plt.figure(figsize=(12,6))

top_states = df["Patient_State"].value_counts().head(10)

ax = sns.barplot(
    x=top_states.values,
    y=top_states.index,
    palette="viridis"
)

plt.title("Top 10 States by Number of Claims", fontsize=16, fontweight="bold")
plt.xlabel("Claims")
plt.ylabel("State")

for p in ax.patches:
    ax.annotate(
        f'{int(p.get_width()):,}',
        (p.get_width(), p.get_y()+p.get_height()/2),
        va='center'
    )

plt.show()

# ==========================================================
# 8. Especialidades Médicas
# ==========================================================

plt.figure(figsize=(12,6))

specialty = df["Provider_Specialty"].value_counts()

ax = sns.barplot(
    x=specialty.values,
    y=specialty.index,
    palette="plasma"
)

plt.title("Provider Specialty Distribution", fontsize=16, fontweight="bold")
plt.xlabel("Claims")

plt.show()

# ==========================================================
# 9. Estadísticas Numéricas
# ==========================================================

print(df.describe().T)


# ==========================================================
# BLOQUE 4 - BUSINESS ORIENTED EDA
# ==========================================================

print("=" * 80)
print("BUSINESS ORIENTED EXPLORATORY DATA ANALYSIS")
print("=" * 80)

# ==========================================================
# 1. Fraud Rate
# ==========================================================

fraud_rate = df["Is_Fraud"].value_counts(normalize=True) * 100

print("\nFraud Rate (%)")
print(fraud_rate.round(2))

# ==========================================================
# 2. Claim Amount by Fraud
# ==========================================================

plt.figure(figsize=(10,6))

sns.boxplot(
    data=df,
    x="Is_Fraud",
    y="Claim_Amount",
    palette="viridis"
)

plt.title("Claim Amount by Fraud Status", fontsize=16, fontweight="bold")
plt.xlabel("Fraud")
plt.ylabel("Claim Amount ($)")

plt.show()

# ==========================================================
# 3. Approved Amount by Fraud
# ==========================================================

plt.figure(figsize=(10,6))

sns.boxplot(
    data=df,
    x="Is_Fraud",
    y="Approved_Amount",
    palette="magma"
)

plt.title("Approved Amount by Fraud Status", fontsize=16, fontweight="bold")
plt.xlabel("Fraud")
plt.ylabel("Approved Amount ($)")

plt.show()

# ==========================================================
# 4. Patient Age by Fraud
# ==========================================================

plt.figure(figsize=(10,6))

sns.boxplot(
    data=df,
    x="Is_Fraud",
    y="Patient_Age",
    palette="plasma"
)

plt.title("Patient Age by Fraud Status", fontsize=16, fontweight="bold")

plt.show()

# ==========================================================
# 5. Fraud Rate by Insurance Type
# ==========================================================

insurance_fraud = (
    df.groupby("Insurance_Type")["Is_Fraud"]
      .mean()
      .sort_values(ascending=False)
      * 100
)

plt.figure(figsize=(10,6))

ax = sns.barplot(
    x=insurance_fraud.values,
    y=insurance_fraud.index,
    palette="viridis"
)

plt.title("Fraud Rate by Insurance Type", fontsize=16, fontweight="bold")
plt.xlabel("Fraud Rate (%)")

for p in ax.patches:
    ax.annotate(
        f"{p.get_width():.1f}%",
        (p.get_width(), p.get_y()+p.get_height()/2),
        va="center"
    )

plt.show()

# ==========================================================
# 6. Fraud Rate by Provider Specialty
# ==========================================================

specialty_fraud = (
    df.groupby("Provider_Specialty")["Is_Fraud"]
      .mean()
      .sort_values(ascending=False)
      * 100
)

plt.figure(figsize=(12,6))

ax = sns.barplot(
    x=specialty_fraud.values,
    y=specialty_fraud.index,
    palette="rocket"
)

plt.title("Fraud Rate by Provider Specialty", fontsize=16, fontweight="bold")
plt.xlabel("Fraud Rate (%)")

plt.show()

# ==========================================================
# 7. Top 10 States with Highest Fraud Rate
# ==========================================================

state_fraud = (
    df.groupby("Patient_State")["Is_Fraud"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
      * 100
)

plt.figure(figsize=(10,6))

ax = sns.barplot(
    x=state_fraud.values,
    y=state_fraud.index,
    palette="crest"
)

plt.title("Top 10 States by Fraud Rate", fontsize=16, fontweight="bold")
plt.xlabel("Fraud Rate (%)")

for p in ax.patches:
    ax.annotate(
        f"{p.get_width():.1f}%",
        (p.get_width(), p.get_y()+p.get_height()/2),
        va="center"
    )

plt.show()

# ==========================================================
# 8. Chronic Condition vs Fraud
# ==========================================================

plt.figure(figsize=(8,5))

ax = sns.countplot(
    data=df,
    x="Chronic_Condition_Flag",
    hue="Is_Fraud",
    palette="viridis"
)

plt.title("Fraud by Chronic Condition", fontsize=16, fontweight="bold")

plt.show()

# ==========================================================
# 9. Length of Stay vs Fraud
# ==========================================================

plt.figure(figsize=(10,6))

sns.boxplot(
    data=df,
    x="Is_Fraud",
    y="Length_of_Stay",
    palette="coolwarm"
)

plt.title("Length of Stay by Fraud Status", fontsize=16, fontweight="bold")

plt.show()

# ==========================================================
# 10. Correlation Matrix
# ==========================================================

plt.figure(figsize=(12,10))

corr = df.select_dtypes(include="number").corr()

sns.heatmap(
    corr,
    annot=True,
    cmap="viridis",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Correlation Matrix", fontsize=18, fontweight="bold")

plt.show()