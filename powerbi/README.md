# 📊 Power BI — Healthcare Fraud Intelligence

This folder contains the Power BI reporting layer of the **Healthcare Fraud Detection & Executive Intelligence** project.

The objective is to translate analytical and machine learning outputs into an executive-oriented reporting experience.

---

## 🎯 Objective

The dashboard is designed to move from:

```text
KPI
 ↓
Pattern
 ↓
Risk
 ↓
Investigation
```

rather than presenting a collection of disconnected charts.

---

## 📊 Executive KPIs

The reporting layer includes metrics such as:

- Total Claims
- Claimed Amount
- Approved Amount
- Rejected Amount
- Fraud Cases
- Fraud Rate
- Avg. Claim Amount
- Avg. Approved Amount
- Recoverable Amount
- Fraud Risk

---

## 🔍 Fraud Intelligence

The dashboard supports analysis across:

### Medical Specialty
`Fraud Rate by Medical Specialty`

### Diagnosis
`Fraud Cases by Diagnosis`

### Insurance
`Fraud Rate by Insurance Type`

### Visit Type
`Fraud Rate by Visit Type`

### Geography
`Fraud Cases & Claimed Amount by State`

---

## 🏥 Provider Intelligence

The provider section focuses on patterns such as:

- Top Providers by Fraud Cases
- Provider fraud rate
- High-risk providers
- Provider-level claim exposure

---

## ⚠️ Risk Intelligence

Risk views include:

- Claim Risk Distribution
- High-risk claims
- Fraud probability / prediction outputs where available
- Financial exposure associated with suspicious claims

---

## 🤖 Machine Learning Integration

Python generates structured outputs such as:

```text
ml_predictions.csv
model_metrics.csv
high_risk_claims.csv
feature_importance.csv
shap_values.csv
```

The SQL layer also contains dedicated ML integration objects.

This creates a modular flow:

```text
Python ML
    ↓
Predictions / Results
    ↓
SQL Analytical Layer
    ↓
Power BI
```

The current portfolio version keeps these components modular and does not require a live SQL Server → Power BI connection.

---

## 🧮 DAX & Data Modeling

The report uses:

- DAX measures
- Business-oriented display names
- Data modeling
- KPI cards
- Gauges
- Analytical charts
- Executive summaries

Underlying database field names can remain unchanged while visible Power BI labels are presented in recruiter-friendly English.

---

## 🗂️ Power BI Folder

Recommended structure:

```text
power_bi/
├── Healthcare_Fraud_Detection_Executive_Intelligence.pbix
└── README.md
```

The PBIX file is the interactive reporting artifact.

---

## 📸 Documentation

Dashboard screenshots are maintained separately in:

```text
screenshots/
```

Selected visuals used inside documentation can be stored in:

```text
images/power_bi/
```

Avoid duplicating the same image in both locations.

---

## 👔 Business Perspective

The reporting layer is designed to help stakeholders answer:

- How much fraud is being detected?
- What is the fraud rate?
- Which areas show higher exposure?
- Which providers show notable fraud patterns?
- What claims may warrant further investigation?
- What is the potential financial exposure?

Power BI therefore acts as the **executive intelligence layer** of the project.
