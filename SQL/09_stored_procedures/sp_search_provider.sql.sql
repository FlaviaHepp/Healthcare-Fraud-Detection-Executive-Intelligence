--Search provider

CREATE PROCEDURE sp_SearchProvider

@ProviderID VARCHAR(20)

AS

BEGIN

SET NOCOUNT ON;

SELECT *

FROM dbo.healthcare_claims

WHERE Provider_ID = @ProviderID;

END;