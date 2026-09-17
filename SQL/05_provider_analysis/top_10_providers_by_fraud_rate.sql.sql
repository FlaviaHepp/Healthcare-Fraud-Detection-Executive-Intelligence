--Top 10 providers by fraud rate
WITH ProviderFraud AS (

    SELECT

        Provider_ID,

        COUNT(*) AS Total_Claims,

        SUM(Is_Fraud) AS Fraud_Cases,

        ROUND(
            SUM(Is_Fraud) * 100.0 / COUNT(*),
            2
        ) AS Fraud_Rate

    FROM dbo.healthcare_claims

    GROUP BY Provider_ID

)

SELECT TOP (10) *

FROM ProviderFraud

ORDER BY Fraud_Rate DESC,
         Fraud_Cases DESC;