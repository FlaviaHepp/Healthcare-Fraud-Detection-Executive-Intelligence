/*
    Dimension Table: Procedures
*/

USE [HealthcareFraudAnalytics];
GO

IF OBJECT_ID(N'dbo.dim_procedures', N'U') IS NULL
BEGIN
    CREATE TABLE dbo.dim_procedures
    (
        Procedure_Code INT NOT NULL,
        CONSTRAINT PK_dim_procedures
            PRIMARY KEY (Procedure_Code)
    );
END;
GO
