--Executive KPIs table
DROP TABLE IF EXISTS dbo.executive_kpis;
GO

CREATE TABLE dbo.executive_kpis
(
    KPI_Name VARCHAR(100),
    KPI_Value DECIMAL(18,2),
    Last_Update DATETIME DEFAULT GETDATE()
);
GO

TRUNCATE TABLE dbo.executive_kpis;

INSERT INTO dbo.executive_kpis (KPI_Name, KPI_Value)

SELECT 'Total Claims', COUNT(*)
FROM dbo.healthcare_claims

UNION ALL

SELECT 'Fraud Cases', SUM(Is_Fraud)
FROM dbo.healthcare_claims

UNION ALL

SELECT 'Fraud Rate (%)',
ROUND(SUM(Is_Fraud)*100.0/COUNT(*),2)
FROM dbo.healthcare_claims

UNION ALL

SELECT 'Total Claimed',
SUM(Claim_Amount)
FROM dbo.healthcare_claims

UNION ALL

SELECT 'Total Approved',
SUM(Approved_Amount)
FROM dbo.healthcare_claims

UNION ALL

SELECT 'Average Claim',
AVG(Claim_Amount)
FROM dbo.healthcare_claims;

SELECT *
FROM dbo.executive_kpis;