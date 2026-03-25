
-- CLEAN RESET (safe + idempotent)
-- TRUNCATE clears the entire table in a single operation.
--handles foreign keys safely(eg: If you try to delete from vendor_role first, PostgreSQL will block you.because vendor_user has a foreign key reference to it.)
---------------------------------------------------------

TRUNCATE TABLE vendor_user RESTART IDENTITY CASCADE; -- resets auto‑increment IDs (when using RESTART IDENTITY)
TRUNCATE TABLE vendor_role RESTART IDENTITY CASCADE;
TRUNCATE TABLE vendors CASCADE;-- vendor_id is TEXT, so no identity reset
TRUNCATE TABLE addresses CASCADE;

-- FIX vendor FK when i changed the table name to addresses
ALTER TABLE vendors
DROP CONSTRAINT IF EXISTS vendors_address_id_fkey;

ALTER TABLE vendors
ADD CONSTRAINT vendors_address_id_fkey
FOREIGN KEY (address_id) REFERENCES addresses(address_id);


-- SEED vendor_role

INSERT INTO vendor_role (role_name)
VALUES
    ('Vendor Admin'),
    ('Vendor Manager'),
    ('Vendor Worker');


-- SEED vendor_user (local vendor-only users)

INSERT INTO vendor_user (username, password, email, role_id)
VALUES
    ('local_vendor_admin', 'admin123', 'local_admin@vendor.com', 1),
    ('local_vendor_manager', 'manager123', 'local_manager@vendor.com', 2),
    ('local_vendor_worker', 'worker123', 'local_worker@vendor.com', 3);

-- SEED address
INSERT INTO addresses (address_id, street, city, state, zip, country)
VALUES
    ('ADDR001', '123 Main St', 'Houston', 'TX', '77001', 'US'),
    ('ADDR002', '456 Field Rd', 'Dallas', 'TX', '75001', 'US');

-- SEED vendors

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
    description,
    created_at,
    address_id
)
VALUES
    ('V001', 'ABC Oil Services', 'ABC001', NOW(), NULL, 'active', 'VEND001', TRUE, 'approved', 'Primary vendor',NOW(),'ADDR001'),
    ('V002', 'XYZ Field Ops', 'XYZ001', NOW(), NULL, 'active', 'VEND002', FALSE, 'pending', 'Secondary vendor',NOW(),'ADDR002');
   
ALTER TABLE vendors
ADD COLUMN IF NOT EXISTS address_id TEXT;


ALTER TABLE address RENAME TO addresses;

