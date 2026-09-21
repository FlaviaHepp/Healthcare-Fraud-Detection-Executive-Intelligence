/*
    Schema Context
    The project uses SQL Server's default dbo schema.

    This script verifies that the database context and dbo schema
    are available before table creation.
*/

USE [HealthcareFraudAnalytics];
GO

IF SCHEMA_ID(N'dbo') IS NULL
BEGIN
    EXEC(N'CREATE SCHEMA dbo AUTHORIZATION dbo');
END;
GO

SELECT
    SCHEMA_NAME(schema_id) AS Schema_Name
FROM sys.schemas
WHERE name = N'dbo';
GO
