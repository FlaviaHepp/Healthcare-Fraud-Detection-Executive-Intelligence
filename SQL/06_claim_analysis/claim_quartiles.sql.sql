--Claim quartiles
SELECT

    Claim_ID,

    Claim_Amount,

    NTILE(4) OVER(
        ORDER BY Claim_Amount
    ) AS Claim_Quartile

FROM dbo.healthcare_claims;