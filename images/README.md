# Images

This folder contains visual assets used in project documentation and presentation.

## Purpose

The images support both technical and business communication across the repository.

## Suggested Structure

```text
images/
├── architecture/
├── machine_learning/
├── sql/
└── power_bi/
```

### `architecture/`
End-to-end analytical architecture and workflow diagrams.

### `machine_learning/`
Model comparison, confusion matrices, ROC curves, feature importance, and SHAP visualizations.

### `sql/`
Database and data-model diagrams.

### `power_bi/`
Selected dashboard visuals used in README documentation.

## Usage

Images can be embedded in Markdown, for example:

```md
![Model Explainability](images/machine_learning/shap_summary.png)
```

Complete dashboard galleries should remain in `screenshots/` rather than being duplicated here.
