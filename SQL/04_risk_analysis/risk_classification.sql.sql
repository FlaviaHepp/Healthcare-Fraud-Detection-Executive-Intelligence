--Risk classication

SELECT

Claim_ID,

Claim_Amount,

CASE

WHEN Claim_Amount >= 2000 THEN 'Critical'

WHEN Claim_Amount >= 1000 THEN 'High'

WHEN Claim_Amount >= 500 THEN 'Medium'

ELSE 'Low'

END AS Risk_Level

FROM dbo.healthcare_claims;