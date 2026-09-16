--Speciality Performance View
CREATE VIEW vw_Specialty_Performance AS

SELECT

Provider_Specialty,

COUNT(*) AS Claims,

SUM(Is_Fraud) AS Fraud_Cases,

ROUND(
SUM(Is_Fraud)*100.0/COUNT(*),
2
) AS Fraud_Rate,

AVG(Claim_Amount) AS Avg_Claim

FROM dbo.healthcare_claims

GROUP BY Provider_Specialty;