
CREATE SCHEMA IF NOT EXISTS core;

-- ENUMS MUST COME FIRST
CREATE TYPE core.vendor_status AS ENUM ('active', 'inactive', 'suspended');
CREATE TYPE core.compliance_status AS ENUM ('approved', 'pending', 'rejected');



-- vendor_role table
CREATE TABLE IF NOT EXISTS vendor_role (
    role_id     SERIAL PRIMARY KEY,
    role_name   TEXT NOT NULL
);

-- vendor_user table
CREATE TABLE IF NOT EXISTS vendor_user (
    user_id    SERIAL PRIMARY KEY,
    username   VARCHAR(256) NOT NULL,
    password   VARCHAR(256) NOT NULL,
    email      VARCHAR(256) NOT NULL,
    role_id    INTEGER NOT NULL REFERENCES vendor_role(role_id)
);



-- user table
CREATE TABLE IF NOT EXISTS users (
    user_id   SERIAL PRIMARY KEY,
    username  VARCHAR(256) NOT NULL,
    password  VARCHAR(256) NOT NULL,
    email     VARCHAR(256) NOT NULL,
    type      VARCHAR(64)  NOT NULL,
    created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- sessions table
CREATE TABLE IF NOT EXISTS sessions (
    session_id     TEXT PRIMARY KEY,
    user_id        INTEGER NOT NULL REFERENCES "users"(user_id),
    created_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_activity  TIMESTAMP,
    user_agent     TEXT,
    is_active      BOOLEAN DEFAULT TRUE
);

-- vendor table
CREATE TABLE IF NOT EXISTS vendors (
    vendor_id          TEXT PRIMARY KEY,
    company_name       VARCHAR(64),
    company_code       TEXT NOT NULL UNIQUE,
    start_date         TIMESTAMP,
    end_date           TIMESTAMP,
    status             core.vendor_status NOT NULL,
    vendor_code        TEXT NOT NULL UNIQUE,
    onboarding         BOOLEAN DEFAULT FALSE,
    compliance_doc     core.compliance_status NOT NULL,
    description        TEXT,
    created_at         TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



