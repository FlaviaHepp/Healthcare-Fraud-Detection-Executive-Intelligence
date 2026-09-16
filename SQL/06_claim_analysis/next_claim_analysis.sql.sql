--Next claim analysis
SELECT

    Claim_Submission_Date,

    Claim_Amount,

    LEAD(Claim_Amount)

    OVER(

        ORDER BY Claim_Submission_Date

    ) AS Next_Claim

FROM dbo.healthcare_claims;