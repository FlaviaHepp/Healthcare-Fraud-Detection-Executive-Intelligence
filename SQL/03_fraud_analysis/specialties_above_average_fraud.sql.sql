--Specialties aboves average fraud
WITH SpecialtyFraud AS (

    SELECT

        Provider_Specialty,

        ROUND(
            SUM(Is_Fraud) * 100.0 / COUNT(*),
            2
        ) AS Fraud_Rate

    FROM dbo.healthcare_claims

    GROUP BY Provider_Specialty

)

SELECT *

FROM SpecialtyFraud

WHERE Fraud_Rate >

(

SELECT AVG(Fraud_Rate)

FROM SpecialtyFraud

)

ORDER BY Fraud_Rate DESC;