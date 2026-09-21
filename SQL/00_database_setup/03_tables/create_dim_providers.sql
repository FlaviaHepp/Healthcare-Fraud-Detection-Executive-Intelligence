/*
    Dimension Table: Providers
*/

USE [HealthcareFraudAnalytics];
GO

IF OBJECT_ID(N'dbo.dim_providers', N'U') IS NULL
BEGIN
    CREATE TABLE dbo.dim_providers
    (
        Provider_ID VARCHAR(20) NOT NULL,
        Provider_Specialty VARCHAR(100) NULL,

        CONSTRAINT PK_dim_providers
            PRIMARY KEY (Provider_ID)
    );
END;
GO
