# 🏥 Healthcare Fraud Detection & Executive Intelligence

> **End-to-End Data Analytics & Machine Learning Platform for Healthcare Fraud Detection**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![SQL](https://img.shields.io/badge/SQL-Analytics-orange?logo=postgresql)
![Power BI](https://img.shields.io/badge/Power%20BI-Business%20Intelligence-yellow?logo=powerbi)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Predictive%20Analytics-purple)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 🚀 Overview

**Healthcare Fraud Detection & Executive Intelligence** is an end-to-end analytics project designed to detect potentially fraudulent healthcare claims and transform machine learning outputs into actionable business intelligence.

The project combines **Python, Machine Learning, SQL and Power BI** into a unified analytical workflow:

```text
Healthcare Claims Data
        │
        ▼
┌──────────────────────┐
│ Python               │
│ Data Preparation     │
│ Feature Engineering  │
│ Machine Learning     │
│ Model Evaluation     │
│ Explainability       │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ SQL                  │
│ Data Modeling        │
│ Dimensions & Facts   │
│ Analytical Queries   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Power BI             │
│ Executive KPIs       │
│ Fraud Analytics      │
│ Risk Intelligence    │
└──────────────────────┘
```

The objective is not only to **predict fraud**, but also to make the results understandable and useful for business decision-making.

---

# 🎯 Business Problem

Healthcare fraud represents a significant financial and operational risk for insurers and healthcare organizations.

Traditional rule-based approaches may struggle to identify complex patterns across:

* Claim characteristics
* Provider behavior
* Diagnosis and procedure combinations
* Insurance information
* Transaction patterns
* Historical fraud indicators
* Geographic and operational variables

This project addresses the problem through a **data-driven fraud detection framework** capable of identifying suspicious claims and translating analytical results into executive-level insights.

---

# 💡 Project Objectives

### 1. Detect potentially fraudulent claims

Develop and evaluate machine learning models capable of classifying healthcare claims as fraudulent or legitimate.

### 2. Identify relevant fraud patterns

Analyze the characteristics and behavioral patterns associated with suspicious claims.

### 3. Build an analytical data model

Organize healthcare claim information into a structured SQL dimensional model suitable for analytics and reporting.

### 4. Explain model predictions

Use explainability techniques to understand which variables contribute to fraud predictions.

### 5. Create executive intelligence

Transform analytical results into Power BI dashboards that allow stakeholders to monitor fraud risk and investigate business patterns.

---

# 🧠 Analytical Architecture

The project follows a modular analytics architecture:

```text
                    ┌─────────────────────┐
                    │ Healthcare Claims   │
                    │       Dataset       │
                    └──────────┬──────────┘
                               │
                               ▼
                 ┌─────────────────────────┐
                 │        PYTHON            │
                 │                         │
                 │ • Data Preprocessing    │
                 │ • Exploratory Analysis  │
                 │ • Feature Engineering   │
                 │ • Model Training        │
                 │ • Evaluation            │
                 │ • Hyperparameter Tuning │
                 │ • Explainability        │
                 │ • Business Insights     │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │          SQL            │
                 │                         │
                 │ • Fact Table            │
                 │ • Dimension Tables      │
                 │ • Relationships         │
                 │ • Analytical Queries    │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │        POWER BI         │
                 │                         │
                 │ • KPIs                  │
                 │ • Fraud Rate             │
                 │ • Risk Analysis          │
                 │ • Provider Intelligence │
                 │ • Executive Dashboard   │
                 └─────────────────────────┘
```

---

# 🐍 Machine Learning Pipeline

The Python workflow is organized into modular blocks:

| Block | Component             | Purpose                                  |
| ----- | --------------------- | ---------------------------------------- |
| 01–02 | Data Preprocessing    | Load, clean and prepare the dataset      |
| 03–04 | Exploratory Analysis  | Identify distributions and patterns      |
| 05    | Feature Engineering   | Create analytical features               |
| 06    | Preprocessing         | Encoding, imputation and scaling         |
| 07    | Model Training        | Train multiple ML algorithms             |
| 08    | Evaluation            | Compare model performance                |
| 09    | Hyperparameter Tuning | Optimize the selected model              |
| 10    | Explainability        | Interpret model predictions              |
| 11    | Business Insights     | Translate results into business findings |
| 12    | Export Results        | Save models and analytical outputs       |

### 🤖 Models Evaluated

The project benchmarks multiple machine learning algorithms:

* Logistic Regression
* Random Forest
* XGBoost
* LightGBM
* CatBoost

This allows model performance to be compared from both a predictive and business perspective.

---

# 🔍 Model Evaluation

The models are evaluated using classification metrics relevant to fraud detection, including:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC
* Confusion Matrix

For fraud detection, **Recall and Precision are particularly important**, since incorrectly classifying fraudulent claims can have significant financial consequences while excessive false positives can increase investigation costs.

---

# 🧠 Model Explainability

The project incorporates model explainability techniques to move beyond simply predicting fraud.

The objective is to answer:

> **Why was this claim classified as potentially fraudulent?**

Explainability analysis helps identify the variables and patterns that contribute most strongly to model predictions.

This provides greater transparency and supports the transition from a **black-box prediction system** toward actionable fraud intelligence.

---

# 🗄️ SQL Data Model

The SQL layer organizes the healthcare data using a dimensional analytical model.

### Fact Table

```text
fact_claims
```

Contains the transactional healthcare claim information used for analytical reporting.

### Dimension Tables

```text
dim_claim_status
dim_diagnosis
dim_insurance
dim_procedures
dim_providers
dim_states
dim_visit_types
```

The dimensional structure improves analytical organization and allows Power BI to work with a structured business-oriented data model.

### 🔗 Key Relationships

The fact table connects to relevant dimensions through foreign keys such as:

```text
fact_claims
   │
   ├── Diagnosis_Code ──────► dim_diagnosis
   ├── Insurance_Type ──────► dim_insurance
   ├── Procedure_Code ──────► dim_procedures
   ├── Provider_ID ─────────► dim_providers
   ├── Claim_Status ────────► dim_claim_status
   ├── State ───────────────► dim_states
   └── Visit_Type ──────────► dim_visit_types
```

---

# 📊 Power BI Executive Intelligence

The Power BI layer converts the analytical results into an executive monitoring environment.

The dashboard focuses on questions such as:

### Fraud Performance

* How many claims are potentially fraudulent?
* What is the overall fraud rate?
* What is the financial exposure?
* How does fraud vary across categories?

### Provider Intelligence

* Which providers present higher risk?
* Are there unusual provider-level patterns?
* Where should investigations be prioritized?

### Claim Intelligence

* Which claim characteristics are associated with higher fraud risk?
* Which diagnoses or procedures show suspicious behavior?
* Which insurance categories present greater exposure?

### Executive Monitoring

The dashboard is designed to allow stakeholders to move from:

**KPI → Pattern → Risk → Investigation**

rather than simply displaying descriptive charts.

---

# 📈 Business Value

This project demonstrates how data can support a fraud detection strategy across the complete analytics lifecycle.

### Financial Impact

Potentially identify suspicious claims earlier and prioritize investigation resources.

### Operational Efficiency

Support fraud analysts by ranking or highlighting higher-risk claims and patterns.

### Decision Intelligence

Provide executives with a centralized view of fraud indicators and risk exposure.

### Explainable Analytics

Combine predictive modeling with interpretable insights rather than relying exclusively on model outputs.

---

# 🛠️ Technology Stack

### Programming & Analytics

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* LightGBM
* CatBoost
* SHAP
* LIME
* Matplotlib
* Seaborn

### Database & Analytics

* SQL
* PostgreSQL
* Dimensional Modeling
* Analytical Queries

### Business Intelligence

* Microsoft Power BI
* DAX
* Data Modeling
* Executive Dashboards

### Development

* Git
* GitHub
* Modular Python Architecture

---

# 📁 Repository Structure

```text
Healthcare-Fraud-Detection-Executive-Intelligence/
│
├── Python/
│   ├── data_preprocessing.py
│   ├── exploratory_analysis.py
│   ├── feature_engineering.py
│   ├── preprocessing.py
│   ├── model_training.py
│   ├── evaluation.py
│   ├── hyperparameter_tuning.py
│   ├── explainability.py
│   ├── business_insights.py
│   ├── export_results.py
│   └── README.md
│
├── SQL/
│   ├── tables/
│   ├── relationships/
│   ├── analysis/
│   └── README.md
│
├── Power_BI/
│   ├── dashboard/
│   ├── measures/
│   └── README.md
│
├── Screenshots/
│   └── README.md
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🔬 End-to-End Workflow

```text
1. DATA
   ↓
2. CLEANING & PREPROCESSING
   ↓
3. EXPLORATORY DATA ANALYSIS
   ↓
4. FEATURE ENGINEERING
   ↓
5. MACHINE LEARNING
   ↓
6. MODEL EVALUATION
   ↓
7. HYPERPARAMETER OPTIMIZATION
   ↓
8. MODEL EXPLAINABILITY
   ↓
9. BUSINESS INSIGHTS
   ↓
10. SQL ANALYTICS
   ↓
11. POWER BI EXECUTIVE INTELLIGENCE
```

---

# 📸 Dashboard Preview

> Screenshots and dashboard previews are available in the [`Screenshots`](./Screenshots) folder.

### Executive Fraud Intelligence

*Add the final Power BI dashboard screenshot here.*

```text
[ POWER BI DASHBOARD PREVIEW ]
```

---

# 📌 Key Takeaway

**Healthcare Fraud Detection & Executive Intelligence** demonstrates an end-to-end approach to modern data analytics:

> **From raw healthcare claims → machine learning → explainable predictions → SQL analytics → executive decision intelligence.**

The project combines **predictive analytics, data engineering, business intelligence and explainable AI** to address a realistic business problem.

---

# 👩‍💻 Author

**Flavia Hepp**

Data Analyst | Advanced Analytics | Machine Learning | SQL | Power BI | Python

GitHub: [FlaviaHepp](https://github.com/FlaviaHepp)

---

# ⭐ Why This Project Matters

This project was built to demonstrate practical capabilities across the complete analytics lifecycle:

**Data → Analysis → Machine Learning → Explainability → SQL → BI → Business Decision**

Rather than treating Machine Learning, SQL and Power BI as isolated technologies, the project integrates them into a single analytical solution designed around a real business problem.
