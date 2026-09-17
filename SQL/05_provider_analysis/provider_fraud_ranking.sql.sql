--Provider fraud ranking
SELECT

    Provider_ID,

    SUM(Claim_Amount) AS Total_Claimed,

    RANK() OVER(
        ORDER BY SUM(Claim_Amount) DESC
    ) AS Provider_Rank

FROM dbo.healthcare_claims

GROUP BY Provider_ID

ORDER BY Provider_Rank;