--Machine Learning Predictions

DROP TABLE IF EXISTS dbo.ml_predictions;
GO

CREATE TABLE dbo.ml_predictions
(
    Claim_ID VARCHAR(50),

    Actual_Label INT,

    Predicted_Label INT,

    Fraud_Probability FLOAT
);
GO