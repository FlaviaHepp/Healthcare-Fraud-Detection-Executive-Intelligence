--Fraud by diagnosis
SELECT

    Diagnosis_Code,

    COUNT(*) AS Total_Claims,

    SUM(Is_Fraud) AS Fraud_Cases,

    ROUND(
        SUM(Is_Fraud) * 100.0 / COUNT(*),
        2
    ) AS Fraud_Rate

FROM dbo.healthcare_claims

GROUP BY Diagnosis_Code

ORDER BY Fraud_Rate DESC;