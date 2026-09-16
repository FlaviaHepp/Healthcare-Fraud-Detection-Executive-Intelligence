--Total claimed amount
SELECT
SUM(Claim_Amount) AS Total_Claim_Amount
FROM dbo.healthcare_claims;