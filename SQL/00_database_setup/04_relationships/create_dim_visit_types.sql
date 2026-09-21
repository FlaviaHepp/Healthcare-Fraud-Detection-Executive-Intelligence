/*
    Dimension Table: Visit Types
*/

USE [HealthcareFraudAnalytics];
GO

IF OBJECT_ID(N'dbo.dim_visit_types', N'U') IS NULL
BEGIN
    CREATE TABLE dbo.dim_visit_types
    (
        Visit_Type VARCHAR(30) NOT NULL,
        CONSTRAINT PK_dim_visit_types
            PRIMARY KEY (Visit_Type)
    );
END;
GO
