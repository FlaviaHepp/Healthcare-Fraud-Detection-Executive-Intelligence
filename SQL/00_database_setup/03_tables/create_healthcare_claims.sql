/*
    Central Claims Table
    Used by the analytical and reporting SQL scripts.
*/

USE [HealthcareFraudAnalytics];
GO

IF OBJECT_ID(N'dbo.healthcare_claims', N'U') IS NULL
BEGIN
    CREATE TABLE dbo.healthcare_claims
    (
        Claim_ID VARCHAR(20) NOT NULL,
        Provider_ID VARCHAR(20) NULL,
        Insurance_Type VARCHAR(50) NULL,
        Diagnosis_Code VARCHAR(20) NULL,
        Procedure_Code INT NULL,
        Patient_State VARCHAR(50) NULL,
        Visit_Type VARCHAR(30) NULL,
        Claim_Status VARCHAR(30) NULL,
        Patient_Age INT NULL,
        Patient_Gender VARCHAR(20) NULL,
        Claim_Amount DECIMAL(18, 2) NULL,
        Approved_Amount DECIMAL(18, 2) NULL,
        Claim_Submission_Date DATE NULL,
        Days_Between_Service_and_Claim INT NULL,
        Number_of_Claims_Per_Provider_Monthly INT NULL,
        Length_of_Stay INT NULL,
        Chronic_Condition_Flag BIT NULL,
        Prior_Visits_12m INT NULL,
        Is_Fraud BIT NULL,

        CONSTRAINT PK_healthcare_claims
            PRIMARY KEY (Claim_ID)
    );
END;
GO
