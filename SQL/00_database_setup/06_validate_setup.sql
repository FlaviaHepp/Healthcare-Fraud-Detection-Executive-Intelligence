/*
    Database Setup Validation
*/

USE [HealthcareFraudAnalytics];
GO

SELECT
    t.name AS Table_Name,
    t.create_date
FROM sys.tables AS t
WHERE t.name IN
(
    'healthcare_claims',
    'dim_claim_status',
    'dim_diagnosis',
    'dim_insurance',
    'dim_procedures',
    'dim_providers',
    'dim_states',
    'dim_visit_types'
)
ORDER BY t.name;
GO

SELECT
    fk.name AS Foreign_Key,
    OBJECT_NAME(fk.parent_object_id) AS Child_Table,
    OBJECT_NAME(fk.referenced_object_id) AS Parent_Table
FROM sys.foreign_keys AS fk
WHERE fk.parent_object_id = OBJECT_ID(N'dbo.healthcare_claims')
ORDER BY fk.name;
GO
