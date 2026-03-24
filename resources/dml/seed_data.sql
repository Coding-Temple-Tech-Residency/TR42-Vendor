---------------------------------------------------------
-- CLEAN RESET (safe + idempotent)
---------------------------------------------------------
TRUNCATE TABLE sessions RESTART IDENTITY CASCADE;
TRUNCATE TABLE vendor_user RESTART IDENTITY CASCADE;
TRUNCATE TABLE vendor_role RESTART IDENTITY CASCADE;
TRUNCATE TABLE vendors RESTART IDENTITY CASCADE;
TRUNCATE TABLE users RESTART IDENTITY CASCADE;

---------------------------------------------------------
-- SEED vendor_role
---------------------------------------------------------
INSERT INTO vendor_role (role_name)
VALUES
    ('Vendor Admin'),
    ('Vendor Manager'),
    ('Vendor Worker');

---------------------------------------------------------
-- SEED vendor_user (local vendor-only users)
---------------------------------------------------------
INSERT INTO vendor_user (username, password, email, role_id)
VALUES
    ('local_vendor_admin', 'admin123', 'local_admin@vendor.com', 1),
    ('local_vendor_manager', 'manager123', 'local_manager@vendor.com', 2),
    ('local_vendor_worker', 'worker123', 'local_worker@vendor.com', 3);

---------------------------------------------------------
-- SEED users (global users)
---------------------------------------------------------
INSERT INTO users (username, password, email, type)
VALUES
    ('vendor_admin1', 'pass123', 'admin1@vendor.com', 'vendor'),
    ('vendor_manager1', 'pass456', 'manager1@vendor.com', 'vendor'),
    ('vendor_worker1', 'pass789', 'worker1@vendor.com', 'vendor');

---------------------------------------------------------
-- SEED vendors
---------------------------------------------------------
INSERT INTO vendors (
    vendor_id,
    company_name,
    company_code,
    start_date,
    end_date,
    status,
    vendor_code,
    onboarding,
    compliance_doc,
    description
)
VALUES
    ('V001', 'ABC Oil Services', 'ABC001', NOW(), NULL, 'active', 'VEND001', TRUE, 'approved', 'Primary vendor'),
    ('V002', 'XYZ Field Ops', 'XYZ001', NOW(), NULL, 'active', 'VEND002', FALSE, 'pending', 'Secondary vendor');

---------------------------------------------------------
-- SEED sessions
---------------------------------------------------------
INSERT INTO sessions (session_id, user_id, created_at, last_activity, user_agent, is_active)
VALUES
    ('sess_admin_001', 1, NOW(), NOW(), 'Mozilla/5.0', TRUE),
    ('sess_manager_001', 2, NOW(), NOW(), 'Mozilla/5.0', TRUE),
    ('sess_worker_001', 3, NOW(), NOW(), 'Mozilla/5.0', TRUE);
