--State claim ranking CTE
WITH StateRanking AS (

SELECT

Patient_State,

SUM(Claim_Amount) AS Total_Claimed

FROM dbo.healthcare_claims

GROUP BY Patient_State

)

SELECT

Patient_State,

Total_Claimed,

RANK() OVER(

ORDER BY Total_Claimed DESC

) AS State_Rank

FROM StateRanking;