--Classify claims by amount
SELECT

    Claim_ID,

    Provider_ID,

    Claim_Amount,

    ROW_NUMBER() OVER(
        ORDER BY Claim_Amount DESC
    ) AS Claim_Order

FROM dbo.healthcare_claims;