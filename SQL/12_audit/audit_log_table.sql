--Audit table
DROP TABLE IF EXISTS dbo.audit_log;
GO

CREATE TABLE dbo.audit_log
(
    Audit_ID INT IDENTITY(1,1) PRIMARY KEY,

    Execution_Date DATETIME DEFAULT GETDATE(),

    Process_Name VARCHAR(100),

    Records_Affected INT
);