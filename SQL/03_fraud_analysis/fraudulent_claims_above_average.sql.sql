--Fraudulent claims above average
WITH AvgFraudClaim AS (

SELECT

AVG(Claim_Amount) AS AvgFraud

FROM dbo.healthcare_claims

WHERE Is_Fraud = 1

)

SELECT

Claim_ID,

Provider_ID,

Claim_Amount

FROM dbo.healthcare_claims

CROSS JOIN AvgFraudClaim

WHERE

Is_Fraud = 1

AND Claim_Amount > AvgFraud

ORDER BY Claim_Amount DESC;