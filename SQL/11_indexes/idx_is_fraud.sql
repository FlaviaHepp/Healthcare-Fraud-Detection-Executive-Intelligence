/*
    Index: IX_IsFraud
    Purpose:
    Improves query performance when filtering or aggregating
    healthcare claims by fraud status.
*/

CREATE INDEX IX_IsFraud
ON dbo.fact_claims (Is_Fraud);