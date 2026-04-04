CREATE SCHEMA IF NOT EXISTS core;

-- Drop old enums safely
-- DROP TYPE IF EXISTS core.vendor_status CASCADE;
-- DROP TYPE IF EXISTS core.compliance_status CASCADE;
-- DROP TYPE IF EXISTS core.user_type CASCADE;

DROP TABLE vendor_user CASCADE;
DROP TABLE vendor CASCADE;
DROP TABLE address CASCADE;
DROP TABLE "user" CASCADE;

DROP TYPE core.vendor_status CASCADE;
DROP TYPE core.compliance_status CASCADE;
DROP TYPE core.user_type CASCADE;

-- ENUMS MUST COME FIRST
CREATE TYPE core.vendor_status AS ENUM ('active', 'inactive', 'suspended');
CREATE TYPE core.compliance_status AS ENUM ('expired', 'incomplete', 'complete');
CREATE TYPE core.user_type AS ENUM ('operator', 'vendor', 'contractor');

-- ADDRESS TABLE
CREATE TABLE IF NOT EXISTS address (
    address_id VARCHAR(36) PRIMARY KEY,
    street VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    zipcode VARCHAR(20) NOT NULL,
    country VARCHAR(100) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by VARCHAR(100),
    updated_by VARCHAR(100)
);

-- USER TABLE (must come before vendor_user)
CREATE TABLE IF NOT EXISTS "user" (
    user_id VARCHAR(36) PRIMARY KEY,
    username VARCHAR(40) UNIQUE NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    password VARCHAR(400) NOT NULL,
    email VARCHAR(40) UNIQUE NOT NULL,
    type core.user_type NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    is_admin BOOLEAN DEFAULT FALSE,
    profile_photo VARCHAR(200),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by VARCHAR(36) NOT NULL,
    updated_by VARCHAR(36) NOT NULL
);

-- VENDOR TABLE (must come before vendor_user)
CREATE TABLE vendor (
    vendor_id VARCHAR(36) PRIMARY KEY,
    company_name VARCHAR(80) NOT NULL UNIQUE,
    company_code VARCHAR,
    company_email VARCHAR NOT NULL,
    company_phone VARCHAR NOT NULL,
    primary_contact_name VARCHAR,
    address_id VARCHAR(36) UNIQUE REFERENCES address(address_id) ON DELETE CASCADE,
    service_type VARCHAR(100),
    status core.vendor_status NOT NULL DEFAULT 'active',
    compliance_status core.compliance_status DEFAULT 'incomplete',
    onboarding BOOLEAN NOT NULL DEFAULT TRUE,
    description VARCHAR,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- vendor_user table (must come last)
CREATE TABLE IF NOT EXISTS vendor_user (
    id VARCHAR(36) PRIMARY KEY,
    user_id VARCHAR(36) NOT NULL REFERENCES "user"(user_id),
    vendor_id VARCHAR(36) REFERENCES vendor(vendor_id),
    role VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(36) NOT NULL,
    updated_by VARCHAR(36) NOT NULL
);