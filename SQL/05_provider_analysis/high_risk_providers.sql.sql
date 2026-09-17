--High risk providers

WITH ProviderRisk AS (

SELECT

    Provider_ID,

    COUNT(*) AS Claims,

    SUM(Is_Fraud) AS Fraud_Cases,

    ROUND(

        SUM(Is_Fraud) * 100.0 / COUNT(*),

        2

    ) AS Fraud_Rate

FROM dbo.healthcare_claims

GROUP BY Provider_ID

)

SELECT

*,

CASE

WHEN Fraud_Rate >= 20 THEN 'Critical Risk'

WHEN Fraud_Rate >= 10 THEN 'High Risk'

WHEN Fraud_Rate >= 5 THEN 'Medium Risk'

ELSE 'Low Risk'

END AS Risk_Level

FROM ProviderRisk

ORDER BY Fraud_Rate DESC;