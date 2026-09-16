--Check duplicates

SELECT

Claim_ID,

COUNT(*) AS Total

FROM dbo.healthcare_claims

GROUP BY Claim_ID

HAVING COUNT(*) > 1;