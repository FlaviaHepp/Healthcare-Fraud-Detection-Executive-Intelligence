--Total rejected amount
SELECT
SUM(Claim_Amount - Approved_Amount) AS Total_Rejected_Amount
FROM dbo.healthcare_claims;