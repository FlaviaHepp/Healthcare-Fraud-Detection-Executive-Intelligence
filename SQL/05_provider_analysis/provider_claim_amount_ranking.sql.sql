--Provider claim amount ranking

SELECT

    Provider_ID,

    SUM(Is_Fraud) AS Fraud_Cases,

    DENSE_RANK() OVER(
        ORDER BY SUM(Is_Fraud) DESC
    ) AS Fraud_Rank

FROM dbo.healthcare_claims

GROUP BY Provider_ID

ORDER BY Fraud_Rank;