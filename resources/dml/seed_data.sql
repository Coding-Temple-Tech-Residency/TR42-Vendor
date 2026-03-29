
-- CLEAN RESET (safe + idempotent)
-- TRUNCATE clears the entire table in a single operation.
--handles foreign keys safely(eg: If you try to delete from vendor_user first, PostgreSQL will block you.because vendor has a foreign key reference to it.)
---------------------------------------------------------

TRUNCATE TABLE vendor_user RESTART IDENTITY CASCADE; -- resets auto‑increment IDs (when using RESTART IDENTITY)


INSERT INTO vendor_user (
    id,
    user_id,
    vendor_id,
    role,
    created_at,
    updated_at,
    created_by,
    updated_by
) VALUES (
    'user-001-admin',
    'user-001',
    'vendor-001',
    'admin',
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP,
    'system',
    'system'
);
