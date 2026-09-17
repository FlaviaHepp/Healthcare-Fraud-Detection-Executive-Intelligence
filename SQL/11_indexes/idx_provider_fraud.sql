/*
    Index: IX_ProviderFraud
    Purpose:
    Improves query performance for provider-level fraud analysis
    by combining Provider_ID and Is_Fraud.
*/

CREATE INDEX IX_ProviderFraud
ON dbo.fact_claims (Provider_ID, Is_Fraud);