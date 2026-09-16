--States highest fraud and claimed amount
WITH StateSummary AS (

SELECT

Patient_State,

SUM(Is_Fraud) AS Fraud_Cases,

SUM(Claim_Amount) AS Total_Claimed

FROM dbo.healthcare_claims

GROUP BY Patient_State

)

SELECT *

FROM StateSummary

ORDER BY

Fraud_Cases DESC,

Total_Claimed DESC;