# Raw Data

This folder contains the original source dataset used by the Healthcare Fraud Detection & Executive Intelligence project.

## Expected Dataset

```text
healthcare_fraud_detection.csv
```

Recommended location:

```text
data/raw/healthcare_fraud_detection.csv
```

The Python workflow should load the dataset using a repository-relative path.

## Data Policy

Only include the full source dataset when:

- redistribution is permitted by the dataset license;
- it does not contain confidential or personally identifiable healthcare information;
- the file size is appropriate for GitHub.

When the dataset cannot be redistributed, keep this folder limited to this README and document the source and acquisition instructions here.

## Role in the Workflow

```text
Raw Data
   ↓
Data Validation
   ↓
Preprocessing
   ↓
Feature Engineering
   ↓
Machine Learning
```

The raw dataset should not be manually modified. Transformations belong in the Python preprocessing workflow and generated datasets belong in `data/processed/`.
