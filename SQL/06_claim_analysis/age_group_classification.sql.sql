--Age group classification

SELECT

CASE

WHEN Patient_Age < 18 THEN 'Child'

WHEN Patient_Age < 40 THEN 'Young Adult'

WHEN Patient_Age < 60 THEN 'Adult'

ELSE 'Senior'

END AS Age_Group,

COUNT(*) AS Claims

FROM dbo.healthcare_claims

GROUP BY

CASE

WHEN Patient_Age < 18 THEN 'Child'

WHEN Patient_Age < 40 THEN 'Young Adult'

WHEN Patient_Age < 60 THEN 'Adult'

ELSE 'Senior'

END;