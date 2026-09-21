# Database Setup

This folder contains the scripts required to recreate the SQL Server database structure used by the project.

## Setup Order

Run the scripts in this order:

```text
1. 01_create_database.sql
2. 02_create_schema.sql
3. 03_tables/
4. 04_relationships/
5. 05_seed_data/  (optional)
```

## Data Model

The central claims table is:

```text
dbo.healthcare_claims
```

Dimensions:

```text
dbo.dim_claim_status
dbo.dim_diagnosis
dbo.dim_insurance
dbo.dim_procedures
dbo.dim_providers
dbo.dim_states
dbo.dim_visit_types
```

## Why These Folders Exist

### `03_tables/`
Defines the database tables and their primary keys.

### `04_relationships/`
Defines foreign-key relationships from `healthcare_claims` to the dimension tables.

### `05_seed_data/`
Reserved for approved, non-sensitive sample data. The repository should not contain confidential healthcare records.

## Important

Do not upload SQL Server physical database files such as:

```text
.mdf
.ldf
.bak
```

The repository should recreate the database through SQL scripts instead.
