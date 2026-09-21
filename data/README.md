# Data

This folder contains the datasets and data-preparation artifacts used throughout the **Healthcare Fraud Detection & Executive Intelligence** project.

## Purpose

The data layer supports the workflow:

`Raw Claims Data → Cleaning → Feature Engineering → Machine Learning → SQL Analytics → Power BI`

## Structure

```text
data/
├── raw/
└── processed/
```

### `raw/`
Original source data used by the project. Raw data should only be included when redistribution is permitted and no sensitive or personally identifiable information is exposed.

### `processed/`
Cleaned and transformed datasets prepared for analytics and machine learning.

Typical transformations include missing-value handling, duplicate checks, type standardization, validation, feature transformation, and model-ready preparation.

## Data Model

The workflow is centered on healthcare claims and includes information related to claims, providers, diagnoses, procedures, insurance, visit types, patient demographics, claim amounts, historical utilization, and fraud indicators.

The SQL layer organizes this information around a central `fact_claims` table and supporting dimension tables.

## Data Governance

This repository should not contain confidential healthcare records, credentials, database backups, or production-sensitive assets.

## Reproducibility

Use the Python preprocessing workflow to reproduce the transformations applied to the source data before model training.

