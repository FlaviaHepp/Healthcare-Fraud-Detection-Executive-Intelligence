--Check approved greater than claim

SELECT *

FROM dbo.healthcare_claims

WHERE Approved_Amount > Claim_Amount;