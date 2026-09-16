--Speciality financial loss analysis

WITH FinancialLoss AS (

SELECT

Provider_Specialty,

SUM(Claim_Amount) AS Claimed,

SUM(Approved_Amount) AS Approved

FROM dbo.healthcare_claims

GROUP BY Provider_Specialty

)

SELECT

Provider_Specialty,

Claimed,

Approved,

Claimed - Approved AS Financial_Loss

FROM FinancialLoss

ORDER BY Financial_Loss DESC;