/*
    Dimension Table: States
*/

USE [HealthcareFraudAnalytics];
GO

IF OBJECT_ID(N'dbo.dim_states', N'U') IS NULL
BEGIN
    CREATE TABLE dbo.dim_states
    (
        Patient_State VARCHAR(50) NOT NULL,
        CONSTRAINT PK_dim_states
            PRIMARY KEY (Patient_State)
    );
END;
GO
