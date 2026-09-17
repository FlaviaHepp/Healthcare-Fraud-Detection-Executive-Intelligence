/*
    Index: IX_ProviderFraud
    Purpose:
    Improves query performance for provider-level fraud analysis
    by combining Provider_ID and Is_Fraud.
*/

IF NOT EXISTS (
    SELECT 1
    FROM sys.indexes
    WHERE name = 'IX_ProviderFraud'
      AND object_id = OBJECT_ID('dbo.fact_claims')
)
BEGIN
    CREATE INDEX IX_ProviderFraud
    ON dbo.fact_claims (Provider_ID, Is_Fraud);
END;