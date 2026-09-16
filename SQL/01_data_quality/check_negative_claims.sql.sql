--Check negative claims

SELECT *

FROM dbo.healthcare_claims

WHERE Claim_Amount < 0

OR Approved_Amount < 0;