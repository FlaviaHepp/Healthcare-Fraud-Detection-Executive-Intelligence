# 📊 Power BI — Healthcare Fraud Intelligence

## Overview

The **Power BI layer** transforms the analytical outputs of the Healthcare Fraud Detection project into an interactive business intelligence environment.

The dashboard is designed to provide an executive view of:

* Fraud activity
* Claim volume
* Fraud rates
* Financial exposure
* Provider risk
* Claim characteristics
* Geographic patterns
* Operational indicators

The objective is to move from **raw analytical results to actionable business intelligence**.

---

## 🎯 Dashboard Objectives

The Power BI solution answers key business questions:

### Fraud Monitoring

* How many claims are potentially fraudulent?
* What percentage of claims are associated with fraud?
* What is the estimated financial exposure?
* How does fraud evolve across different categories?

### Risk Analysis

* Which providers present higher fraud risk?
* Which procedures or diagnoses are associated with suspicious claims?
* Which insurance categories show greater exposure?
* Which geographic areas require additional attention?

### Executive Decision Support

The dashboard allows stakeholders to quickly identify:

**What is happening → Where is the risk → What requires attention**

---

# 🧩 Data Model

The Power BI model is based on the SQL analytical structure.

### Fact Table

```text
fact_claims
```

Contains the healthcare claim-level transactional information.

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

The dimensional structure supports filtering and analysis across multiple business perspectives.

---

# 🔗 Data Relationships

The model follows a fact-and-dimension architecture.

```text
                    ┌───────────────────┐
                    │ dim_claim_status  │
                    └─────────┬─────────┘
                              │
                              │
┌───────────────────┐         ▼
│  dim_diagnosis    │────► fact_claims ◄────┌──────────────────┐
└───────────────────┘                       │ dim_providers    │
                                           └──────────────────┘
                              ▲
                              │
┌───────────────────┐         │         ┌──────────────────┐
│ dim_insurance     │─────────┘         │ dim_procedures   │
└───────────────────┘                   └──────────────────┘
```

This structure provides a clean foundation for interactive reporting.

---

# 📐 DAX Measures

The dashboard uses DAX measures to calculate the principal KPIs.

### Total Transactions

```DAX
Total Transactions =
COUNTROWS(fact_claims)
```

### Fraud Cases

```DAX
Fraud Cases =
COUNTROWS(
    FILTER(
        fact_claims,
        fact_claims[is_fraud_num] = 1
    )
)
```

### Fraud Rate

```DAX
Fraud Rate % =
DIVIDE(
    [Fraud Cases],
    [Total Transactions],
    0
)
```

These measures allow the dashboard to dynamically respond to filters and slicers.

---

# 📌 Executive KPIs

The dashboard focuses on high-value indicators such as:

| KPI                | Business Purpose                    |
| ------------------ | ----------------------------------- |
| Total Claims       | Measure overall claim volume        |
| Fraud Cases        | Quantify detected suspicious claims |
| Fraud Rate         | Monitor relative fraud prevalence   |
| Financial Exposure | Estimate potential financial impact |
| Provider Risk      | Identify higher-risk providers      |
| Geographic Risk    | Identify areas requiring attention  |

---

# 📊 Dashboard Components

The Power BI solution includes analytical views focused on different aspects of fraud detection.

### Executive Overview

Provides a high-level summary of fraud activity and financial exposure.

### Fraud Analysis

Explores fraud patterns across claim characteristics and business dimensions.

### Provider Intelligence

Highlights provider-level risk patterns and potential investigation priorities.

### Geographic Analysis

Allows fraud activity to be explored across geographic dimensions.

### Claim Analysis

Provides detailed analysis of claim characteristics associated with suspicious activity.

---

# 🎨 Dashboard Design Principles

The dashboard follows an executive-oriented design approach:

* Limited number of high-value KPIs
* Clear visual hierarchy
* Concise chart titles
* Consistent terminology
* Interactive filtering
* Emphasis on risk indicators
* Reduced visual clutter
* Business-oriented storytelling

The goal is not to display every available metric, but to highlight the information most relevant to decision-making.

---

# 🔍 Analytical Questions

The dashboard enables users to investigate questions such as:

> Which providers require additional investigation?

> Which procedures have higher fraud exposure?

> Where is fraud concentrated geographically?

> How significant is fraud relative to total claims?

> Which segments represent the greatest financial risk?

---

# 🚀 Business Impact

The Power BI layer converts technical analytics into an environment that can be used by non-technical stakeholders.

Instead of requiring users to interpret Python models or SQL queries directly, the dashboard provides a visual interface for:

**Monitoring → Investigation → Prioritization → Decision-making**

---

# 🗂️ Files

The Power BI folder contains the dashboard-related assets used in the project.

```text
Power_BI/
│
├── dashboard/
│   └── Healthcare_Fraud_Intelligence.pbix
│
├── measures/
│   └── DAX_Measures.md
│
└── README.md
```

> File names may vary depending on the final repository structure.

---

# 🔄 Integration with the Project

Power BI represents the final analytical layer:

```text
Python
   ↓
Machine Learning & Insights
   ↓
SQL
   ↓
Analytical Data Model
   ↓
Power BI
   ↓
Executive Intelligence
```

This integration demonstrates an end-to-end approach combining:

**Python + Machine Learning + SQL + Power BI**

---

# 📈 Final Objective

The ultimate objective of the dashboard is to help transform fraud detection from a purely technical task into a **business intelligence and risk management process**.

> **Detect the risk. Understand the pattern. Prioritize the investigation. Support the decision.**
