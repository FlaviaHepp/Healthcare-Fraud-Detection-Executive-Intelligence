--Provider Risk View
CREATE VIEW vw_Provider_Risk AS

SELECT

Provider_ID,

COUNT(*) AS Total_Claims,

SUM(Is_Fraud) AS Fraud_Cases,

ROUND(
SUM(Is_Fraud)*100.0/COUNT(*),
2
) AS Fraud_Rate,

SUM(Claim_Amount) AS Total_Claimed

FROM dbo.healthcare_claims

GROUP BY Provider_ID;