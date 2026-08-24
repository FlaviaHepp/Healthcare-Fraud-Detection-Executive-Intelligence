# 🏥 Healthcare Fraud Detection & Executive Intelligence

> **End-to-end healthcare fraud analytics platform combining SQL, Machine Learning, Explainable AI and Power BI to detect suspicious claims, quantify financial risk and transform predictive models into actionable business intelligence.**

---

## 🎯 Project Overview

Healthcare fraud represents a significant financial and operational challenge for insurance companies and healthcare organizations.

This project develops an end-to-end analytical solution designed to identify potentially fraudulent healthcare claims, evaluate model performance, explain prediction drivers and translate analytical results into executive-level insights.

The solution combines:

* **SQL** for relational data architecture and data integrity
* **Python** for data preparation, exploratory analysis and Machine Learning
* **Explainable AI** for model transparency
* **Power BI** for executive reporting and fraud intelligence
* **Statistical and business analysis** to support risk-based decision making

The objective is not only to predict fraud, but to answer a more important business question:

> **Where is fraud risk concentrated, what drives it, and what financial impact could it represent?**

---

# 🧠 Analytical Architecture

```text
                        HEALTHCARE CLAIMS DATA
                                  │
                                  ▼
                         ┌─────────────────┐
                         │      SQL        │
                         │ Data Architecture│
                         │  Star Schema     │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │     PYTHON      │
                         │                 │
                         │ Data Processing │
                         │ Feature Eng.    │
                         │ ML Modeling     │
                         │ Evaluation      │
                         │ Hyperparameter  │
                         │ Optimization    │
                         └────────┬────────┘
                                  │
                    ┌─────────────┼─────────────┐
                    ▼             ▼             ▼
               Predictions      SHAP      Feature Importance
                    │             │             │
                    └─────────────┼─────────────┘
                                  ▼
                         ┌─────────────────┐
                         │    POWER BI     │
                         │                 │
                         │ Fraud Analytics │
                         │ Risk Monitoring │
                         │ Executive BI    │
                         └─────────────────┘
```

---

# 🔍 Business Problem

Healthcare claims can contain complex patterns associated with fraudulent activity.

Traditional rule-based approaches may struggle to detect nonlinear relationships and interactions between:

* Claim amounts
* Provider behavior
* Diagnosis and procedures
* Insurance type
* Patient characteristics
* Historical claims
* Visit patterns
* Length of stay
* Prior utilization
* Geographic information

A Machine Learning approach can identify complex patterns and prioritize suspicious claims for further investigation.

---

# 🚀 Solution

The project implements a complete fraud detection workflow:

### 1. Data Architecture

A relational SQL model was designed around a central claims fact table and supporting dimensions.

### 2. Data Preparation

Python is used to:

* Clean and validate the dataset
* Handle missing values
* Encode categorical variables
* Prepare numerical features
* Detect relevant patterns and anomalies

### 3. Feature Engineering

Additional analytical features are created to capture behavioral and financial patterns associated with potential fraud.

### 4. Machine Learning

Multiple classification algorithms are evaluated and benchmarked.

The modeling workflow includes:

* Logistic Regression
* Random Forest
* XGBoost
* LightGBM
* CatBoost

Models are evaluated using fraud-detection-oriented metrics rather than relying exclusively on accuracy.

### 5. Hyperparameter Optimization

The best-performing models are further optimized using hyperparameter search techniques to improve predictive performance.

### 6. Explainable AI

Model predictions are interpreted using Explainable AI techniques, including:

* SHAP
* Feature Importance
* Model-level interpretation
* Claim-level risk interpretation

This allows the project to move from:

> **"The model predicts fraud."**

to:

> **"The model predicts fraud because these factors are driving the risk."**

### 7. Business Intelligence

Machine Learning outputs are transformed into executive-level Power BI dashboards for:

* Fraud monitoring
* Risk prioritization
* Financial exposure analysis
* Model performance monitoring
* High-risk claim investigation
* Explainability analysis

---

# 📊 Key Analytical Questions

The platform is designed to answer questions such as:

### Fraud Risk

* How frequently does fraud occur?
* Which claims have the highest predicted fraud probability?
* Where is fraud risk concentrated?

### Financial Impact

* What is the total claim exposure?
* What amount is potentially recoverable?
* Which suspicious claims represent the greatest financial risk?

### Provider & Claim Behavior

* Which providers show higher levels of suspicious activity?
* Which claim characteristics are associated with fraud?
* Are there recurring patterns among high-risk claims?

### Machine Learning

* Which model performs best?
* How well does the model distinguish fraudulent from legitimate claims?
* Which features have the greatest influence on predictions?

### Explainability

* Why is a claim classified as high risk?
* Which variables increase or decrease fraud probability?
* Can investigators understand the reasoning behind model predictions?

---

# 🤖 Machine Learning Pipeline

```text
Raw Data
   │
   ▼
Data Preprocessing
   │
   ▼
Exploratory Analysis
   │
   ▼
Feature Engineering
   │
   ▼
Preprocessing
   │
   ▼
Model Benchmarking
   │
   ▼
Model Evaluation
   │
   ▼
Hyperparameter Optimization
   │
   ▼
Explainability
   │
   ▼
Business Insights
   │
   ▼
Results Export
```

---

# 🧪 Model Evaluation

The project evaluates classification performance using metrics relevant to fraud detection, including:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC
* Confusion Matrix
* ROC Curve

Particular attention is given to **Recall and Precision**, since fraud detection requires balancing the identification of suspicious claims with the cost of false positives.

---

# 🔬 Explainable AI

Explainability is a core component of the solution.

The project uses SHAP and feature importance techniques to understand model behavior.

This enables analysis at two levels:

### Global Explainability

Understanding which variables have the strongest influence across the model.

### Local Explainability

Understanding why an individual claim receives a high or low fraud prediction.

This is particularly important in financial and healthcare environments where analytical decisions require transparency and traceability.

---

# 💰 Business Intelligence

The Power BI layer converts Machine Learning outputs into business-oriented insights.

The dashboard focuses on:

* Fraud Rate
* Fraud Cases
* Total Claims
* Claim Exposure
* Estimated Recoverable Amount
* High-Risk Claims
* Fraud Probability
* Provider Risk
* Model Performance
* Feature Importance
* Explainability

The objective is to move from **prediction to decision support**.

---

# 🗄️ SQL Data Model

The SQL layer follows a relational star-schema design.

```text
                    dim_claim_status
                           │
                    dim_diagnosis
                           │
                    dim_insurance
                           │
                    dim_procedures
                           │
                    dim_providers
                           │
                    dim_states
                           │
                    dim_visit_types
                           │
                           ▼
                       fact_claims
```

The central `fact_claims` table contains claim-level information, while dimension tables provide structured analytical attributes.

Primary and foreign keys are used to maintain relational integrity.

---

# 🛠️ Technology Stack

| Category              | Technologies                |
| --------------------- | --------------------------- |
| Programming           | Python                      |
| Data Analysis         | Pandas, NumPy               |
| Visualization         | Matplotlib, Seaborn         |
| Machine Learning      | Scikit-learn                |
| Gradient Boosting     | XGBoost, LightGBM, CatBoost |
| Explainable AI        | SHAP                        |
| Database              | SQL Server / T-SQL          |
| Business Intelligence | Power BI                    |
| Model Persistence     | Joblib                      |
| Version Control       | Git / GitHub                |

---

# 📁 Project Structure

```text
Healthcare-Fraud-Detection-Executive-Intelligence/
│
├── README.md
│
├── SQL/
│   ├── README.md
│   ├── 01_create_database.sql
│   ├── 02_create_schema.sql
│   ├── 03_create_tables.sql
│   ├── 04_create_constraints.sql
│   └── 05_validation.sql
│
├── Python/
│   ├── README.md
│   ├── data_preprocessing.py
│   ├── exploratory_analysis.py
│   ├── feature_engineering.py
│   ├── preprocessing.py
│   ├── model_training.py
│   ├── evaluation.py
│   ├── hyperparameter_tuning.py
│   ├── explainability.py
│   ├── business_insights.py
│   └── export_results.py
│
├── PowerBI/
│   ├── README.md
│   └── Healthcare_Fraud_Executive_Dashboard.pbix
│
├── screenshots/
│   ├── README.md
│   ├── executive_overview.png
│   ├── fraud_analysis.png
│   ├── model_performance.png
│   └── explainability.png
│
├── data/
├── models/
├── results/
│
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

# 📸 Dashboard Preview

Visual examples of the analytical dashboards and Machine Learning outputs are available in the [`screenshots/`](screenshots/) folder.

The Power BI layer provides an executive view of fraud exposure, risk concentration, model performance and explainability.

---

# 🎯 Business Impact

The solution is designed to support a risk-based fraud investigation strategy.

Instead of treating every claim equally, the platform can help prioritize:

```text
LOW RISK
   ↓
Routine Monitoring

MEDIUM RISK
   ↓
Additional Review

HIGH RISK
   ↓
Priority Investigation
```

This approach can help organizations focus analytical and investigative resources where the potential financial impact is greatest.

---

# 🔮 Future Improvements

Potential extensions include:

* MLflow experiment tracking
* Model deployment through an API
* Dockerized ML environment
* Automated model retraining
* Real-time fraud scoring
* Cloud deployment
* Data drift monitoring
* Model drift monitoring
* Automated investigation workflows
* LLM-powered fraud investigation assistant
* RAG-based access to fraud investigation policies and documentation

---

# 👩‍💻 Author

**Flavia Hepp**

Data Analytics | Machine Learning | SQL | Python | Power BI

GitHub: [FlaviaHepp](https://github.com/FlaviaHepp)

---

## ⭐ Project Objective

This project demonstrates how **Data Analytics, Machine Learning, Explainable AI, SQL and Business Intelligence can be combined into a complete fraud intelligence solution**.

The ultimate goal is to transform raw healthcare claims data into:

**Data → Predictions → Explainability → Risk → Business Decisions**

