--Executive Dashboard View
DROP VIEW IF EXISTS dbo.vw_PowerBI_ExecutiveDashboard;
GO

CREATE VIEW dbo.vw_PowerBI_ExecutiveDashboard
AS

SELECT

    Claim_ID,
    Provider_ID,
    Claim_Submission_Date,

    Patient_State,

    Provider_Specialty,

    Insurance_Type,

    Visit_Type,

    Patient_Age,

    dbo.fn_AgeGroup(Patient_Age) AS Age_Group,

    Claim_Amount,

    Approved_Amount,

    Claim_Amount - Approved_Amount AS Financial_Loss,

    Is_Fraud,

    dbo.fn_RiskLevel(Claim_Amount) AS Risk_Level,

    Length_of_Stay,

    Prior_Visits_12m

FROM dbo.healthcare_claims;
GO