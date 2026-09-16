--Claims by age group

WITH AgeGroups AS (

SELECT

CASE

WHEN Patient_Age < 18 THEN 'Child'

WHEN Patient_Age < 40 THEN 'Young Adult'

WHEN Patient_Age < 60 THEN 'Adult'

ELSE 'Senior'

END AS Age_Group,

Claim_Amount,

Is_Fraud

FROM dbo.healthcare_claims

)

SELECT

Age_Group,

COUNT(*) AS Claims,

SUM(Is_Fraud) AS Fraud_Cases,

AVG(Claim_Amount) AS Avg_Claim

FROM AgeGroups

GROUP BY Age_Group

ORDER BY Avg_Claim DESC;