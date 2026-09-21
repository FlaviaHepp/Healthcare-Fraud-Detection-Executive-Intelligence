# 🏥 SQL — Healthcare Fraud Analytics

This folder contains the **Microsoft SQL Server / T-SQL** layer of the Healthcare Fraud Detection & Executive Intelligence project.

The SQL implementation is organized by technical purpose so each script has one clear location.

---

## 🗂️ Folder Structure

```text
SQL/
├── 00_database_setup/
├── 01_data_quality/
├── 02_kpi_metrics/
├── 03_fraud_analysis/
├── 04_risk_analysis/
├── 05_provider_analysis/
├── 06_claim_analysis/
├── 07_advanced_sql/
├── 08_views/
├── 09_stored_procedures/
├── 10_functions/
├── 11_indexes/
├── 12_audit/
├── 13_ml_integration/
└── 14_metadata/
```

---

## 00 — Database Setup

Creates the database structure required by the analytical workflow.

```text
00_database_setup/
├── 01_create_database.sql
├── 02_create_schema.sql
├── 03_tables/
├── 04_relationships/
└── 05_seed_data/
```

The setup uses `dbo.healthcare_claims` as the central claims table and dimension tables for reusable descriptive attributes.

---

## 01 — Data Quality

Data validation and consistency checks.

Examples:

- Duplicate claims
- Null values
- Negative claim amounts
- Approved amount greater than claimed amount

---

## 02 — KPI Metrics

Business metrics used by the executive reporting layer.

Examples:

- Total Claims
- Total Claimed Amount
- Total Approved Amount
- Total Rejected Amount
- Fraud Cases
- Fraud Rate
- Average Claim Amount
- Average Approved Amount

---

## 03 — Fraud Analysis

Explores fraud patterns across:

- Diagnosis
- Medical specialty
- Insurance type
- Visit type
- State
- Claim amount

---

## 04 — Risk Analysis

Contains scripts whose primary purpose is claim-level risk classification or risk-oriented scoring.

```text
04_risk_analysis/
└── risk_classification.sql
```

A SQL Server `CREATE INDEX` is not considered a risk metric. Physical database indexes belong in `11_indexes/`.

---

## 05 — Provider Analysis

Provider-focused analytical queries.

Examples:

- Providers with the most fraud cases
- Provider fraud ranking
- Provider claim amount ranking
- Top providers by fraud rate
- High-risk providers

---

## 06 — Claim Analysis

Claim-level segmentation and descriptive analysis.

Examples:

- Claim amount categories
- Claim quartiles
- Claims above average
- Age groups
- Chronic condition analysis
- Average claim by specialty

---

## 07 — Advanced SQL

Advanced analytical patterns such as:

- CTEs
- Ranking logic
- Financial loss analysis
- Multi-step analytical queries

---

## 08 — Views

Reusable SQL views for reporting and analytical consumption.

Examples include:

- Executive dashboard views
- Provider risk view
- Specialty performance view
- Power BI KPI view
- Machine learning dashboard view

---

## 09 — Stored Procedures

Only scripts that create SQL Server stored procedures belong here.

```text
09_stored_procedures/
├── sp_search_provider.sql
├── sp_state_analysis.sql
└── sp_top_fraud_providers.sql
```

---

## 10 — Functions

Reusable scalar or table-valued functions.

Examples:

- Risk-level classification
- Age-group classification

---

## 11 — Indexes

Physical SQL Server indexes used to support query performance.

```text
11_indexes/
├── idx_is_fraud.sql
├── idx_provider_id.sql
├── idx_claim_submission_date.sql
└── idx_provider_fraud.sql
```

These are database-performance objects and should not be mixed with analytical risk indicators.

---

## 12 — Audit

Audit-related structures used to record and monitor database activity.

---

## 13 — ML Integration

SQL objects that connect machine learning outputs with the analytical layer.

Examples:

- ML prediction storage
- ML dashboard views

---

## 14 — Metadata

Documentation metadata such as the SQL data dictionary.

---

## ▶️ Recommended Execution Order

```text
00_database_setup
        ↓
01_data_quality
        ↓
02_kpi_metrics
        ↓
03_fraud_analysis
        ↓
04_risk_analysis
        ↓
05_provider_analysis
        ↓
06_claim_analysis
        ↓
07_advanced_sql
        ↓
08_views
        ↓
09_stored_procedures
        ↓
10_functions
        ↓
11_indexes
        ↓
12_audit
        ↓
13_ml_integration
        ↓
14_metadata
```

Not every analytical script must be run sequentially. The order above reflects the logical organization of the repository.

---

## 🧱 Central Data Model

```text
dbo.healthcare_claims

    ├── Provider_ID ───────► dim_providers
    ├── Insurance_Type ────► dim_insurance
    ├── Diagnosis_Code ─────► dim_diagnosis
    ├── Procedure_Code ─────► dim_procedures
    ├── Patient_State ──────► dim_states
    ├── Visit_Type ─────────► dim_visit_types
    └── Claim_Status ───────► dim_claim_status
```

This structure provides the relational foundation for fraud analysis and reporting.

---

## 💡 Design Principle

A script should appear in **one folder only**.

The classification is based on what the SQL object or query primarily does:

```text
Analytical Risk Metric  → 04_risk_analysis
Provider Analysis       → 05_provider_analysis
Stored Procedure        → 09_stored_procedures
Physical Index          → 11_indexes
```

This avoids duplicated scripts and makes the repository easier to navigate.
