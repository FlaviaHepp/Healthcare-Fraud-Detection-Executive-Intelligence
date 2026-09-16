--Total claimed
SELECT
SUM(Claim_Amount) AS Total_Claimed
FROM healthcare_claims;

--Total approved
SELECT
SUM(Approved_Amount) AS Total_Approved
FROM healthcare_claims;

--Frauds
SELECT
SUM(Is_Fraud) AS Fraud_Cases
FROM healthcare_claims;

--Frauds %
SELECT
100.0 * SUM(Is_Fraud) / COUNT(*) AS Fraud_Rate
FROM healthcare_claims;