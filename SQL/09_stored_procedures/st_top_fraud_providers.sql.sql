--Top fraud providers

CREATE PROCEDURE sp_TopFraudProviders

AS

BEGIN

SET NOCOUNT ON;

SELECT TOP (20)

Provider_ID,

COUNT(*) AS Total_Claims,

SUM(Is_Fraud) AS Fraud_Cases,

ROUND(
SUM(Is_Fraud)*100.0/COUNT(*),
2
) AS Fraud_Rate

FROM dbo.healthcare_claims

GROUP BY Provider_ID

ORDER BY Fraud_Cases DESC;

END;

EXEC sp_TopFraudProviders;