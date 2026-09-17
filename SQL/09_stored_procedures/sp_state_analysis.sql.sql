--Reclamos por estado
CREATE PROCEDURE sp_StateAnalysis

AS

BEGIN

SET NOCOUNT ON;

SELECT

Patient_State,

COUNT(*) AS Claims,

SUM(Is_Fraud) AS Fraud_Cases,

SUM(Claim_Amount) AS Total_Claimed

FROM dbo.healthcare_claims

GROUP BY Patient_State

ORDER BY Total_Claimed DESC;

END;