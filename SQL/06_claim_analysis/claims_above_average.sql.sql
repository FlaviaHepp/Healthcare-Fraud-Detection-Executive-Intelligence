--Claims above average

WITH AvgClaim AS (

SELECT

AVG(Claim_Amount) AS Avg_Claim

FROM dbo.healthcare_claims

)

SELECT

Claim_ID,

Provider_ID,

Claim_Amount

FROM dbo.healthcare_claims

CROSS JOIN AvgClaim

WHERE Claim_Amount > Avg_Claim

ORDER BY Claim_Amount DESC;