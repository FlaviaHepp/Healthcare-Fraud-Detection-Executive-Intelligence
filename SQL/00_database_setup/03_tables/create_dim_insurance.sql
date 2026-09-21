/*
    Dimension Table: Insurance
*/

USE [HealthcareFraudAnalytics];
GO

IF OBJECT_ID(N'dbo.dim_insurance', N'U') IS NULL
BEGIN
    CREATE TABLE dbo.dim_insurance
    (
        Insurance_Type VARCHAR(50) NOT NULL,
        CONSTRAINT PK_dim_insurance
            PRIMARY KEY (Insurance_Type)
    );
END;
GO
