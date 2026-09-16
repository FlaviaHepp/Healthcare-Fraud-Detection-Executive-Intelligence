--Average claim approval difference
SELECT

AVG(Claim_Amount-Approved_Amount)
AS Average_Difference

FROM dbo.healthcare_claims;