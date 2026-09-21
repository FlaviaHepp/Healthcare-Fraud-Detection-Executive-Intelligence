# Processed Data

This folder contains datasets generated after cleaning, validation, and feature preparation.

## Purpose

Processed data provides a reproducible intermediate layer between the raw dataset and downstream machine learning or analytics.

Typical transformations include:

- Data type standardization
- Missing-value treatment
- Duplicate handling
- Validation rules
- Feature engineering
- Encoding and model preparation

## Suggested Files

Depending on the final Python workflow, this folder may contain files such as:

```text
healthcare_claims_clean.csv
ml_ready_claims.csv
```

Only include generated files that are useful for reproducibility or demonstrate an important analytical stage.

## Source

Processed datasets should be generated from:

```text
data/raw/
```

using the scripts in:

```text
python/
```

## Principle

```text
raw/       → source data
processed/ → transformed data
results/   → analytical outputs
models/    → trained model artifacts
```

Keeping these layers separate makes the repository easier to understand and reproduce.
