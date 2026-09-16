--Machine Learning Dashboard
CREATE VIEW vw_PowerBI_ML AS

SELECT

Claim_ID,

Provider_ID,

Claim_Amount,

Approved_Amount,

Is_Fraud,

Length_of_Stay,

Prior_Visits_12m,

Patient_Age

FROM dbo.healthcare_claims;