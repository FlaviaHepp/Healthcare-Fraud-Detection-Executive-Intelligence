--Average hospital stadistics
SELECT

    Visit_Type,

    AVG(Length_of_Stay) AS Avg_Length_of_Stay

FROM dbo.healthcare_claims

GROUP BY Visit_Type;