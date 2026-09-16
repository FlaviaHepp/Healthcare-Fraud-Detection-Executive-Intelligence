--Speciality fraud ranking
SELECT

    Provider_Specialty,

    SUM(Is_Fraud) AS Fraud_Cases,

    RANK() OVER(
        ORDER BY SUM(Is_Fraud) DESC
    ) AS Specialty_Rank

FROM dbo.healthcare_claims

GROUP BY Provider_Specialty

ORDER BY Specialty_Rank;