/*
    Index: IX_ClaimSubmissionDate
    Purpose:
    Improves query performance for date-based analysis,
    filtering, trend analysis, and reporting.
*/

CREATE INDEX IX_ClaimSubmissionDate
ON dbo.fact_claims (Claim_Submission_Date);