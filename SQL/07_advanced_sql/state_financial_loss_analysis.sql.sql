--State financial loss analysis
SELECT

    Patient_State,

    SUM(Claim_Amount) AS Total_Claimed,

    SUM(Approved_Amount) AS Total_Approved,

    SUM(Claim_Amount - Approved_Amount) AS Financial_Loss

FROM dbo.healthcare_claims

GROUP BY Patient_State

ORDER BY Financial_Loss DESC;