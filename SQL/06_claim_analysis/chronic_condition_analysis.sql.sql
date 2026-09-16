--Chronic condition analysis 
SELECT

    Chronic_Condition_Flag,

    COUNT(*) AS Patients,

    SUM(Is_Fraud) AS Fraud_Cases

FROM dbo.healthcare_claims

GROUP BY Chronic_Condition_Flag;