--Function to classify the risk of a claim
CREATE FUNCTION fn_RiskLevel
(

    @ClaimAmount DECIMAL(12,2)

)

RETURNS VARCHAR(20)

AS

BEGIN

    DECLARE @Risk VARCHAR(20)

    SET @Risk =

    CASE

        WHEN @ClaimAmount >= 2000 THEN 'Critical'

        WHEN @ClaimAmount >= 1000 THEN 'High'

        WHEN @ClaimAmount >= 500 THEN 'Medium'

        ELSE 'Low'

    END

    RETURN @Risk

END;