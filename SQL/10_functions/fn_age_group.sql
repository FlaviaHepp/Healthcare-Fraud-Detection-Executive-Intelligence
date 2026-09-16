--Function for age group
CREATE FUNCTION fn_AgeGroup
(

    @Age INT

)

RETURNS VARCHAR(20)

AS

BEGIN

    DECLARE @Group VARCHAR(20)

    SET @Group =

    CASE

        WHEN @Age < 18 THEN 'Child'
        WHEN @Age < 40 THEN 'Young Adult'
        WHEN @Age < 60 THEN 'Adult'
        ELSE 'Senior'

    END

    RETURN @Group

END;

