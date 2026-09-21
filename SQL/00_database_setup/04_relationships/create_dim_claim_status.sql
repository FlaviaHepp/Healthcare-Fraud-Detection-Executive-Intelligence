/*
    Dimension Table: Claim Status
*/

USE [HealthcareFraudAnalytics];
GO

IF OBJECT_ID(N'dbo.dim_claim_status', N'U') IS NULL
BEGIN
    CREATE TABLE dbo.dim_claim_status
    (
        Claim_Status VARCHAR(30) NOT NULL,
        CONSTRAINT PK_dim_claim_status
            PRIMARY KEY (Claim_Status)
    );
END;
GO
