--Providers with most fraud cases
SELECT TOP (20)

    Provider_ID,

    COUNT(*) AS Total_Claims,

    SUM(Is_Fraud) AS Fraud_Cases

FROM dbo.healthcare_claims

GROUP BY Provider_ID

ORDER BY Fraud_Cases DESC;