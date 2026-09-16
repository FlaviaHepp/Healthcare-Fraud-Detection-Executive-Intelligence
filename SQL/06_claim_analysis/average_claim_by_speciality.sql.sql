--Average claim by speciality
SELECT

    Provider_Specialty,

    Claim_ID,

    Claim_Amount,

    AVG(Claim_Amount) OVER(

        PARTITION BY Provider_Specialty

    ) AS Avg_Specialty_Claim

FROM dbo.healthcare_claims;