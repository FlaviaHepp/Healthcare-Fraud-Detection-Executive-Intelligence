--Dashboard Summary
WITH DashboardSummary AS (

SELECT

COUNT(*) AS Total_Claims,

SUM(Is_Fraud) AS Fraud_Cases,

SUM(Claim_Amount) AS Total_Claimed,

SUM(Approved_Amount) AS Total_Approved,

AVG(Claim_Amount) AS Average_Claim

FROM dbo.healthcare_claims

)

SELECT *

FROM DashboardSummary;