CREATE SCHEMA IF NOT EXISTS core;

-- ENUMS MUST COME FIRST
CREATE TYPE core.vendor_status AS ENUM ('active', 'inactive', 'suspended');
CREATE TYPE core.compliance_status AS ENUM ('approved', 'pending', 'rejected');

-- vendor_user table
CREATE TABLE IF NOT EXISTS vendor_user (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    vendor_id TEXT,
    role TEXT,  -- changed from core.role_options
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by TEXT NOT NULL,
    updated_by TEXT NOT NULL
);


