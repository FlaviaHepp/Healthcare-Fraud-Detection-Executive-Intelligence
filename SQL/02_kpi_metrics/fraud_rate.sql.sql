--Fraud rate
SELECT

COUNT(CASE WHEN Is_Fraud = 1 THEN 1 END) * 100.0
/
COUNT(*) AS Fraud_Rate

FROM dbo.healthcare_claims;