/*
    Healthcare Fraud Detection & Executive Intelligence
    Database Creation Script

    Creates the local SQL Server database used by the project.
*/

IF DB_ID(N'HealthcareFraudAnalytics') IS NULL
BEGIN
    EXEC(N'CREATE DATABASE [HealthcareFraudAnalytics]');
END;
GO

USE [HealthcareFraudAnalytics];
GO

SELECT
    DB_NAME() AS Current_Database,
    SUSER_SNAME() AS Current_Login;
GO
