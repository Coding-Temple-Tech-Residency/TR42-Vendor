
-- CLEAN RESET (safe + idempotent)
-- TRUNCATE clears the entire table in a single operation.
--handles foreign keys safely(eg: If you try to delete from vendor_user first, PostgreSQL will block you.because vendor has a foreign key reference to it.)
---------------------------------------------------------

 -- resets auto‑increment IDs (when using RESTART IDENTITY)

TRUNCATE TABLE vendor_user RESTART IDENTITY CASCADE;
TRUNCATE TABLE vendor RESTART IDENTITY CASCADE;
TRUNCATE TABLE address RESTART IDENTITY CASCADE;


-- SEED DATA
INSERT INTO address (address_id, street, city, state, zipcode, country, created_by, updated_by)
VALUES
('ADDR001', '123 Main Street', 'Houston', 'Texas', '77001', 'USA', 'system', 'system'),
('ADDR002', '455 Industrial Park Drive', 'Charlotte', 'North Carolina', '28202', 'USA', 'system', 'system'),
('ADDR003', '88 Summit Ridge Road', 'Denver', 'Colorado', '80202', 'USA', 'system', 'system');

INSERT INTO vendor (
    vendor_id, company_name, company_code, company_email, company_phone,
    primary_contact_name, address_id, service_type, status, compliance_status,
    onboarding, description
)
VALUES
('VEND001', 'Alpha Field Services', 'AFS-001', 'contact@alphafs.com', '+1-919-555-1020',
 'Michael Turner', 'ADDR001', 'Oilfield Maintenance', 'active', 'complete', TRUE,
 'Full‑service field operations provider.'),
('VEND002', 'BlueRock Contractors', 'BRC-204', 'info@bluerockco.com', '+1-704-555-8899',
 'Sarah Mitchell', 'ADDR002', 'Pipeline Inspection', 'inactive', 'incomplete', TRUE,
 'Specializes in pipeline inspection and compliance.'),
('VEND003', 'Summit Industrial Solutions', 'SIS-330', 'support@summitind.com', '+1-980-555-4411',
 'James Carter', 'ADDR003', 'Equipment Installation', 'suspended', 'expired', FALSE,
 'Vendor requires updated compliance documentation.');

INSERT INTO "user" (
    user_id, username, password, email, type,
    is_active, is_admin, created_by, updated_by
)
VALUES
('USER001', 'admin', 'HASHED_PASSWORD', 'admin@example.com', 'operator', TRUE, TRUE, 'system', 'system'),
('USER002', 'john_doe', 'HASHED_PASSWORD', 'john@example.com', 'vendor', TRUE, FALSE, 'system', 'system');

INSERT INTO vendor_user (
    id, user_id, vendor_id, role, created_by, updated_by
)
VALUES
('VU001', 'USER002', 'VEND001', 'admin', 'system', 'system');

-- Check enums

-- SELECT n.nspname AS schema, t.typname AS enum_name
-- FROM pg_type t
-- JOIN pg_namespace n ON n.oid = t.typnamespace
-- WHERE t.typtype = 'e';


-- You should see:

-- core.vendor_status
-- core.compliance_status
-- core.user_type


-- Check vendor_user join

-- SELECT * FROM vendor_user;