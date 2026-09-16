--Executive Dashboard
CREATE VIEW vw_PowerBI_Executive AS

SELECT

Claim_Submission_Date,

Patient_State,

Provider_Specialty,

Insurance_Type,

Visit_Type,

Claim_Amount,

Approved_Amount,

Is_Fraud

FROM dbo.healthcare_claims;