--Check null values

SELECT

SUM(CASE WHEN Insurance_Type IS NULL THEN 1 ELSE 0 END) AS Missing_Insurance,

SUM(CASE WHEN Provider_Specialty IS NULL THEN 1 ELSE 0 END) AS Missing_Specialty,

SUM(CASE WHEN Prior_Visits_12m IS NULL THEN 1 ELSE 0 END) AS Missing_Visits

FROM dbo.healthcare_claims;