-- Power BI KPIs view
DROP VIEW IF EXISTS dbo.vw_KPIs;
GO

CREATE VIEW dbo.vw_KPIs
AS

SELECT *

FROM dbo.executive_kpis;
GO
