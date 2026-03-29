CREATE SCHEMA IF NOT EXISTS core;

-- ENUMS MUST COME FIRST
CREATE TYPE core.role_options AS ENUM ('admin', 'manager', 'supervisor');

-- vendor_user table
CREATE TABLE IF NOT EXISTS vendor_user (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    vendor_id TEXT,
    role core.role_options NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by TEXT NOT NULL,
    updated_by TEXT NOT NULL
);
