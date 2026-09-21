/*
    Dimension Table: Diagnosis
*/

USE [HealthcareFraudAnalytics];
GO

IF OBJECT_ID(N'dbo.dim_diagnosis', N'U') IS NULL
BEGIN
    CREATE TABLE dbo.dim_diagnosis
    (
        Diagnosis_Code VARCHAR(20) NOT NULL,
        CONSTRAINT PK_dim_diagnosis
            PRIMARY KEY (Diagnosis_Code)
    );
END;
GO
