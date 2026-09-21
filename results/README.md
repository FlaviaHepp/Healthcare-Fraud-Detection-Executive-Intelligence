# Results

This folder contains analytical outputs generated throughout the project.

## Purpose

The results layer connects machine learning with the SQL and Power BI layers.

```text
Machine Learning
      ↓
Predictions & Metrics
      ↓
Structured Results
      ↓
SQL Analytics
      ↓
Power BI Executive Intelligence
```

## Main Result Categories

### Model Performance
Comparative metrics for the evaluated machine learning models, including Accuracy, Precision, Recall, F1 Score, and ROC-AUC.

### Predictions
Model outputs such as Claim ID, fraud probability, predicted fraud class, and risk classification.

### Explainability
Feature-importance and SHAP-based outputs used to understand fraud predictions.

### Business Insights
Aggregated findings related to fraud patterns, high-risk claims, provider risk, financial exposure, geographic patterns, and diagnosis or procedure patterns.

## Relationship with Power BI

Python-generated outputs support the analytical and reporting workflow used by the Power BI layer.

## Reproducibility

Results should be regenerated from the scripts in `python/` rather than manually edited. Generated outputs should be documented with their source script and relevant dataset/model version whenever possible.
