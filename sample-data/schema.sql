CREATE SCHEMA "core";

CREATE TYPE "core"."vendor_contractor_roles" AS ENUM ('DRIVER', 'WORKER', 'PRIVATE_CONTRACTOR');

CREATE TYPE "core"."location_type" AS ENUM ('WELL', 'GPS', 'ADDRESS');

CREATE TYPE "core"."frequency_type" AS ENUM ('ONE_TIME', 'DAILY', 'WEEKLY', 'MONTHLY');

CREATE TYPE "core"."role_options" AS ENUM ('USER', 'MANAGER', 'ADMIN');

CREATE TYPE "core"."notification_level" AS ENUM ('SUCCESS', 'DANGER', 'INFO');

CREATE TYPE "core"."device_types" AS ENUM ('ANDROID', 'IOS', 'TABLET', 'OTHER');

CREATE TYPE "core"."note_categories" AS ENUM ('GENERAL', 'SAFETY', 'QUALITY', 'INSTRUCTION');

CREATE TYPE "core"."issue_categories" AS ENUM ('SAFETY', 'QUALITY', 'DELAY', 'OTHER');

CREATE TYPE "core"."issue_severities" AS ENUM ('LOW', 'MEDIUM', 'HIGH', 'CRITICAL', 'BLOCKER');

CREATE TYPE "core"."order_status" AS ENUM (
  'UNASSIGNED',
  'ASSIGNED',
  'IN_PROGRESS',
  'COMPLETED',
  'HALTED',
  'REJECTED',
  'CANCELLED',
  'CLOSED'
);

CREATE TYPE "core"."vendor_status" AS ENUM ('ACTIVE', 'INACTIVE');

CREATE TYPE "core"."compliance_status" AS ENUM ('EXPIRED', 'INCOMPLETE', 'COMPLETE');

CREATE TYPE "core"."priority_status" AS ENUM ('LOW', 'MEDIUM', 'HIGH');

CREATE TYPE "core"."ticket_status" AS ENUM (
  'UNASSIGNED',
  'ASSIGNED',
  'IN_PROGRESS',
  'COMPLETED'
);

CREATE TYPE "core"."well_status" AS ENUM (
  'ACTIVE',
  'DRILLING',
  'COMPLETED',
  'INACTIVE',
  'SUSPENDED',
  'ABANDONED',
  'PLUGGED'
);

CREATE TYPE "core"."well_type" AS ENUM (
  'OIL',
  'GAS',
  'OIL_AND_GAS',
  'INJECTION',
  'WATER_DISPOSAL',
  'OBSERVATION'
);

CREATE TYPE "core"."contractor_status" AS ENUM ('ACTIVE', 'INACTIVE');

CREATE TYPE "core"."company_types" AS ENUM (
  'OIL_GAS_OPERATORS',
  'VENDOR_SERVICE_PROVIDER',
  'FIELD_PERSONNEL'
);

CREATE TYPE "core"."invoice_statuses" AS ENUM (
  'DRAFT',
  'SUBMITTED',
  'APPROVED',
  'REJECTED',
  'PAID'
);

CREATE TYPE "core"."user_type" AS ENUM ('OPERATOR', 'VENDOR', 'CONTRACTOR');

CREATE TABLE
  "client" (
    "id" text PRIMARY KEY,
    "client_name" text NOT NULL,
    "client_code" text NOT NULL,
    "primary_contact_name" text NOT NULL,
    "contact_email" text NOT NULL,
    "contact_phone" text NOT NULL,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL,
    "address_id" text
  );

CREATE TABLE
  "vendor" (
    "id" text PRIMARY KEY,
    "company_name" varchar(80) UNIQUE NOT NULL,
    "company_code" text,
    "start_date" timestamptz,
    "end_date" timestamptz,
    "primary_contact_name" text NOT NULL,
    "company_email" text NOT NULL,
    "company_phone" text NOT NULL,
    "status" core.vendor_status NOT NULL,
    "vendor_code" text,
    "onboarding" bool NOT NULL,
    "compliance_status" core.compliance_status,
    "description" text,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text,
    "updated_by" text,
    "address_id" text
  );

CREATE TABLE
  "address" (
    "id" text PRIMARY KEY,
    "street" text,
    "city" text,
    "state" varchar(20),
    "zip" varchar(10),
    "country" varchar(100),
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "client_vendor" (
    "id" text PRIMARY KEY,
    "client_id" text NOT NULL,
    "vendor_id" text NOT NULL,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "contractors" (
    "id" text PRIMARY KEY,
    "employee_number" text NOT NULL,
    "user_id" text NOT NULL,
    "role" text NOT NULL,
    "status" core.contractor_status,
    "tickets_completed" integer,
    "tickets_open" integer,
    "biometric_enrolled" bool,
    "is_onboarded" bool,
    "is_subcontractor" bool,
    "is_fte" bool,
    "is_licensed" bool,
    "is_insured" bool,
    "is_certified" bool,
    "average_rating" decimal(3, 2),
    "years_experience" integer,
    "preferred_job_types" json,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "vendor_contractor" (
    "id" text PRIMARY KEY,
    "contractor_id" text NOT NULL,
    "vendor_id" text NOT NULL,
    "manager_id" text NOT NULL,
    "vendor_contractor_role" core.vendor_contractor_roles NOT NULL
  );

CREATE TABLE
  "background_check" (
    "id" text PRIMARY KEY,
    "contractor_id" text NOT NULL,
    "background_check_passed" bool,
    "background_check_date" date,
    "background_check_provider" text,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "drug_test" (
    "id" text PRIMARY KEY,
    "contractor_id" text NOT NULL,
    "drug_test_passed" bool,
    "drug_test_date" date,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "biometric_data" (
    "id" text PRIMARY KEY,
    "contractor_id" text NOT NULL,
    "biometric_enrollment_data" bytea,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "licenses" (
    "id" text PRIMARY KEY,
    "contractor_id" text NOT NULL,
    "license_type" varchar(100) NOT NULL,
    "license_number" varchar(100) NOT NULL,
    "license_state" char(2) NOT NULL,
    "license_expiration_date" date NOT NULL,
    "license_document_url" varchar(100),
    "license_verified" bool,
    "license_verified_by" text,
    "license_verified_at" date,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "certifications" (
    "id" text PRIMARY KEY,
    "contractor_id" text NOT NULL,
    "certification_name" text,
    "certifying_body" text,
    "certification_number" text NOT NULL,
    "issue_date" timestamptz NOT NULL,
    "expiration_date" timestamptz,
    "certification_document_url" varchar(100),
    "certification_verified" bool,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "insurance" (
    "id" text PRIMARY KEY,
    "contractor_id" text,
    "insurance_type" text NOT NULL,
    "policy_number" text NOT NULL,
    "provider_name" text NOT NULL,
    "provider_phone" text NOT NULL,
    "coverage_amount" decimal,
    "deductible" decimal,
    "effective_date" date,
    "expiration_date" date,
    "insurance_document_url" varchar(100),
    "insurance_verified" bool NOT NULL,
    "additional_insurance_required" bool,
    "additional_insured_certificate_url" varchar(100),
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "compliance_document" (
    "id" text PRIMARY KEY,
    "vendor_id" text NOT NULL,
    "compliance_document" bytea,
    "compliance_status" bool NOT NULL DEFAULT (false),
    "expiration_date" date,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "msa" (
    "id" text PRIMARY KEY,
    "vendor_id" text NOT NULL,
    "version" varchar(10),
    "effective_date" date,
    "expiration_date" date,
    "status" varchar(15),
    "uploaded_by" text,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "msa_requirements" (
    "id" text PRIMARY KEY,
    "msa_id" text NOT NULL,
    "category" varchar(50),
    "rule_type" varchar(50),
    "description" text,
    "value" varchar(100),
    "unit" varchar(100),
    "source_field_id" text,
    "page_number" int,
    "extracted_text" text,
    "confidence_score" float,
    "metadata" json,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "work_orders" (
    "id" text PRIMARY KEY,
    "assigned_vendor" text,
    "client_id" text NOT NULL,
    "assigned_at" timestamptz,
    "completed_at" timestamptz,
    "description" text,
    "work_order_name" varchar(10) UNIQUE,
    "estimated_start_date" timestamptz,
    "estimated_end_date" timestamptz,
    "current_status" core.order_status NOT NULL,
    "comments" varchar(500),
    "location" varchar(100),
    "location_type" core.location_type,
    "latitude" numeric,
    "longitude" numeric,
    "estimated_cost" decimal,
    "estimated_duration" interval,
    "priority" core.priority_status NOT NULL,
    "well_id" text,
    "service_type" text NOT NULL,
    "estimated_quantity" float,
    "units" varchar(15),
    "is_recurring" boolean,
    "recurrence_type" core.frequency_type,
    "cancelled_at" timestamptz,
    "cancellation_reason" text,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "ticket" (
    "id" text PRIMARY KEY,
    "work_order_id" text NOT NULL,
    "invoice_id" text,
    "description" text NOT NULL,
    "assigned_contractor" text,
    "priority" core.priority_status,
    "status" core.ticket_status,
    "vendor_id" text,
    "start_time" timestamptz,
    "due_date" timestamptz NOT NULL,
    "assigned_at" timestamptz,
    "completed_at" timestamptz,
    "estimated_duration" interval,
    "service_type" text NOT NULL,
    "notes" text,
    "contractor_start_location" text,
    "contractor_end_location" text,
    "estimated_quantity" float,
    "unit" text,
    "special_requirements" text,
    "anomaly_flag" bool,
    "anomaly_reason" text,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL,
    "additional_information" json,
    "route" text
  );

CREATE TABLE
  "contractor_performance" (
    "id" text PRIMARY KEY,
    "contractor_id" text NOT NULL,
    "ticket_id" text UNIQUE NOT NULL,
    "rating" integer,
    "comments" text,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "ticket_session" (
    "id" text PRIMARY KEY,
    "contractor_id" text,
    "ticket_id" text,
    "device_id" text,
    "check_in_time" timestamptz,
    "check_out_time" timestamptz,
    "ticket_accepted" bool,
    "ticket_declined" bool,
    "ticket_completed" bool,
    "location" numeric,
    "notes" text,
    "duration" interval,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "delivery" (
    "id" text PRIMARY KEY,
    "session_id" text NOT NULL,
    "delivery_ticket_number" varchar(50),
    "delivery_date" date,
    "delivery_time" time,
    "delivery_company" varchar(50),
    "driver_name" varchar(60),
    "vehicle_license" varchar(60),
    "delivery_condition" varchar(20),
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "submission" (
    "id" text PRIMARY KEY,
    "session_id" text NOT NULL,
    "submitted_at" timestamptz,
    "submission_status" varchar(50),
    "submission_package_url" text,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "field_note" (
    "id" text PRIMARY KEY,
    "session_id" text NOT NULL,
    "note_text" text,
    "note_timestamp" timestamptz,
    "note_latitude" numeric,
    "note_longitude" numeric,
    "note_category" core.note_categories,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "issue" (
    "id" text PRIMARY KEY,
    "session_id" text NOT NULL,
    "issue_title" varchar(100),
    "issue_description" text,
    "issue_category" core.issue_categories,
    "issue_severity" core.issue_severities,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "registered_devices" (
    "id" text PRIMARY KEY,
    "contractor_id" text NOT NULL,
    "device_name" varchar(100),
    "device_type" core.device_types,
    "first_registered_at" timestamptz,
    "last_used_at" timestamptz,
    "biometric_enabled_on_device" bool,
    "notification_preferences" json,
    "is_active" bool,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "ticket_photos" (
    "id" text PRIMARY KEY,
    "ticket_id" text NOT NULL,
    "photo_content" bytea NOT NULL,
    "latitude" numeric,
    "longitude" numeric,
    "uploaded_by" text NOT NULL,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "invoice" (
    "id" text PRIMARY KEY,
    "work_order_id" text NOT NULL,
    "vendor_id" text NOT NULL,
    "client_id" text NOT NULL,
    "invoice_date" timestamptz NOT NULL,
    "due_date" timestamptz NOT NULL,
    "period_start" timestamptz,
    "period_end" timestamptz,
    "total_amount" decimal,
    "invoice_status" core.invoice_statuses,
    "paid_at" timestamptz,
    "approved_at" timestamptz,
    "rejected_at" timestamptz,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "line_item" (
    "id" text PRIMARY KEY,
    "invoice_id" text NOT NULL,
    "quantity" integer,
    "rate" decimal,
    "amount" decimal,
    "description" text,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "user" (
    "id" text PRIMARY KEY,
    "username" varchar(40) UNIQUE NOT NULL,
    "password_hash" varchar(400) NOT NULL,
    "email" varchar(100) UNIQUE NOT NULL,
    "user_type" core.user_type NOT NULL,
    "token_version" integer DEFAULT 0,
    "is_active" bool NOT NULL DEFAULT true,
    "is_admin" bool DEFAULT false,
    "profile_photo" bytea,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text DEFAULT 'system',
    "updated_by" text DEFAULT 'system',
    "first_name" varchar(80),
    "last_name" varchar(80),
    "middle_name" varchar(80),
    "contact_number" varchar(30),
    "alternate_number" varchar(30),
    "date_of_birth" date,
    "ssn_last_four" char(4),
    "address_id" text
  );

CREATE TABLE
  "client_user" (
    "id" text PRIMARY KEY,
    "user_id" text UNIQUE NOT NULL,
    "client_id" text NOT NULL,
    "role" core.role_options NOT NULL,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "vendor_user" (
    "id" text PRIMARY KEY,
    "user_id" text UNIQUE NOT NULL,
    "vendor_id" text,
    "vendor_user_role" core.role_options,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "sessions" (
    "id" text PRIMARY KEY,
    "user_id" text NOT NULL,
    "last_activity" timestamptz,
    "user_agent" text,
    "is_active" bool,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "notification" (
    "id" text PRIMARY KEY,
    "message" text,
    "recipient" text,
    "level" core.notification_level,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "well" (
    "id" text PRIMARY KEY,
    "api_number" text NOT NULL,
    "well_name" text NOT NULL,
    "client_id" text,
    "status" core.well_status,
    "type" core.well_type,
    "range" char(2),
    "quarter" char(2),
    "ground_elevation" integer,
    "total_depth" integer,
    "geofence_radius" integer,
    "spud_date" timestamptz,
    "completion_date" timestamptz,
    "access_instructions" text,
    "safety_notes" text,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "well_location" (
    "id" text PRIMARY KEY,
    "well_id" text NOT NULL,
    "surface_latitude" numeric,
    "surface_longitude" numeric,
    "bottom_latitude" numeric,
    "bottom_longitude" numeric,
    "county" text,
    "state" char(2),
    "field_name" text,
    "section" integer,
    "township" char(2),
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "vendor_well" (
    "id" text PRIMARY KEY,
    "vendor_id" text NOT NULL,
    "well_id" text NOT NULL,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "services" (
    "id" text PRIMARY KEY,
    "service" text,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "vendor_services" (
    "id" text PRIMARY KEY,
    "vendor_id" text,
    "service_id" text,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "fraud_alerts" (
    "id" text PRIMARY KEY,
    "work_order_id" text,
    "ticket_id" text,
    "severity" varchar(100),
    "description" text,
    "status" text,
    "flagged_at" timestamptz,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "chat" (
    "id" text PRIMARY KEY,
    "messages" text,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

CREATE TABLE
  "messages" (
    "id" text PRIMARY KEY,
    "sender" text,
    "recipient" text,
    "chat_id" text NOT NULL,
    "message" text,
    "created_at" timestamptz DEFAULT (now ()),
    "updated_at" timestamptz,
    "created_by" text NOT NULL,
    "updated_by" text NOT NULL
  );

ALTER TABLE "address" ADD CONSTRAINT "address_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "address" ADD CONSTRAINT "address_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "client" ADD CONSTRAINT "client_address" FOREIGN KEY ("address_id") REFERENCES "address" ("id") DEFERRABLE INITIALLY IMMEDIATE;;

ALTER TABLE "vendor" ADD CONSTRAINT "vendor_address" FOREIGN KEY ("address_id") REFERENCES "address" ("id") DEFERRABLE INITIALLY IMMEDIATE;;

ALTER TABLE "client" ADD CONSTRAINT "client_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "vendor" ADD CONSTRAINT "vendor_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "client" ADD CONSTRAINT "client_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "vendor" ADD CONSTRAINT "vendor_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "client_vendor" ADD CONSTRAINT "client_client_vendor" FOREIGN KEY ("client_id") REFERENCES "client" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "client_vendor" ADD CONSTRAINT "vendor_client_vendor" FOREIGN KEY ("vendor_id") REFERENCES "vendor" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "contractors" ADD CONSTRAINT "contractor_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "contractors" ADD CONSTRAINT "contractor_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "vendor_contractor" ADD CONSTRAINT "vendor_contractor_contractor" FOREIGN KEY ("contractor_id") REFERENCES "contractors" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "vendor_contractor" ADD CONSTRAINT "vendor_contractor_vendor" FOREIGN KEY ("vendor_id") REFERENCES "vendor" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "vendor_contractor" ADD CONSTRAINT "vendor_contractor_manager" FOREIGN KEY ("manager_id") REFERENCES "vendor_user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "background_check" ADD CONSTRAINT "contractor_background_check" FOREIGN KEY ("contractor_id") REFERENCES "contractors" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "drug_test" ADD CONSTRAINT "contractor_drug_test" FOREIGN KEY ("contractor_id") REFERENCES "contractors" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "background_check" ADD CONSTRAINT "background_check_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "background_check" ADD CONSTRAINT "background_check_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "drug_test" ADD CONSTRAINT "drug_test_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "drug_test" ADD CONSTRAINT "drug_test_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "biometric_data" ADD CONSTRAINT "contractor_biometrics" FOREIGN KEY ("contractor_id") REFERENCES "contractors" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "biometric_data" ADD CONSTRAINT "biometric_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "biometric_data" ADD CONSTRAINT "biometric_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "licenses" ADD CONSTRAINT "contractor_license" FOREIGN KEY ("contractor_id") REFERENCES "contractors" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "licenses" ADD CONSTRAINT "vendor_verifier" FOREIGN KEY ("license_verified_by") REFERENCES "vendor" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "licenses" ADD CONSTRAINT "license_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "licenses" ADD CONSTRAINT "license_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "certifications" ADD CONSTRAINT "contractor_certifications" FOREIGN KEY ("contractor_id") REFERENCES "contractors" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "certifications" ADD CONSTRAINT "certifications_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "certifications" ADD CONSTRAINT "certifications_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "insurance" ADD CONSTRAINT "contractor_insurance" FOREIGN KEY ("contractor_id") REFERENCES "contractors" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "insurance" ADD CONSTRAINT "insurance_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "insurance" ADD CONSTRAINT "insurance_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "compliance_document" ADD CONSTRAINT "vendor_compliance" FOREIGN KEY ("vendor_id") REFERENCES "vendor" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "compliance_document" ADD CONSTRAINT "compliance_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "compliance_document" ADD CONSTRAINT "compliance_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "msa" ADD CONSTRAINT "vendor_msa" FOREIGN KEY ("vendor_id") REFERENCES "vendor" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "msa_requirements" ADD CONSTRAINT "msa_msa_requirement" FOREIGN KEY ("msa_id") REFERENCES "msa" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "msa" ADD CONSTRAINT "msa_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "msa" ADD CONSTRAINT "msa_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "msa" ADD CONSTRAINT "msa_uploaded_by" FOREIGN KEY ("uploaded_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "msa_requirements" ADD CONSTRAINT "msa_req_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "msa_requirements" ADD CONSTRAINT "msa_req_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "work_orders" ADD CONSTRAINT "client_work_order" FOREIGN KEY ("client_id") REFERENCES "client" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "work_orders" ADD CONSTRAINT "work_order_service" FOREIGN KEY ("service_type") REFERENCES "services" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "work_orders" ADD CONSTRAINT "vendor_work_order" FOREIGN KEY ("assigned_vendor") REFERENCES "vendor" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "work_orders" ADD CONSTRAINT "work_orders_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "work_orders" ADD CONSTRAINT "work_orders_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "ticket" ADD CONSTRAINT "ticket_service" FOREIGN KEY ("service_type") REFERENCES "services" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "ticket" ADD CONSTRAINT "work_order_tickets" FOREIGN KEY ("work_order_id") REFERENCES "work_orders" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "ticket" ADD CONSTRAINT "contractor_ticket" FOREIGN KEY ("assigned_contractor") REFERENCES "contractors" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "contractor_performance" ADD CONSTRAINT "ticket_contractor_performance" FOREIGN KEY ("ticket_id") REFERENCES "ticket" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "contractor_performance" ADD CONSTRAINT "contractor_ticket_contractor_performance" FOREIGN KEY ("contractor_id") REFERENCES "contractors" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "ticket" ADD CONSTRAINT "vendor_ticket" FOREIGN KEY ("vendor_id") REFERENCES "vendor" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "ticket" ADD CONSTRAINT "ticket_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "ticket" ADD CONSTRAINT "ticket_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "contractor_performance" ADD CONSTRAINT "ratings_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "contractor_performance" ADD CONSTRAINT "ratings_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "ticket_session" ADD CONSTRAINT "ticket_ticket_session" FOREIGN KEY ("ticket_id") REFERENCES "ticket" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "ticket_session" ADD CONSTRAINT "ticket_session_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "ticket_session" ADD CONSTRAINT "ticket_session_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "ticket_session" ADD CONSTRAINT "ticket_session_contractor" FOREIGN KEY ("contractor_id") REFERENCES "contractors" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "field_note" ADD CONSTRAINT "ticket_session_notes" FOREIGN KEY ("session_id") REFERENCES "ticket_session" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "issue" ADD CONSTRAINT "ticket_session_issues" FOREIGN KEY ("session_id") REFERENCES "ticket_session" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "submission" ADD CONSTRAINT "ticket_session_submission" FOREIGN KEY ("session_id") REFERENCES "ticket_session" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "delivery" ADD CONSTRAINT "ticket_session_delivery" FOREIGN KEY ("session_id") REFERENCES "ticket_session" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "delivery" ADD CONSTRAINT "delivery_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "delivery" ADD CONSTRAINT "delivery_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "submission" ADD CONSTRAINT "submission_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "submission" ADD CONSTRAINT "submission_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "field_note" ADD CONSTRAINT "field_note_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "field_note" ADD CONSTRAINT "field_note_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "issue" ADD CONSTRAINT "issue_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "issue" ADD CONSTRAINT "issue_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "ticket_session" ADD CONSTRAINT "device_job_session" FOREIGN KEY ("device_id") REFERENCES "registered_devices" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "registered_devices" ADD CONSTRAINT "contractor_device" FOREIGN KEY ("contractor_id") REFERENCES "contractors" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "registered_devices" ADD CONSTRAINT "device_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "registered_devices" ADD CONSTRAINT "device_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "ticket_photos" ADD CONSTRAINT "ticket_ticket_photos" FOREIGN KEY ("ticket_id") REFERENCES "ticket" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "ticket_photos" ADD CONSTRAINT "ticket_photo_uploaded" FOREIGN KEY ("uploaded_by") REFERENCES "contractors" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "ticket_photos" ADD CONSTRAINT "ticket_photo_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "ticket_photos" ADD CONSTRAINT "ticket_photo_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "invoice" ADD CONSTRAINT "client_invoice" FOREIGN KEY ("client_id") REFERENCES "client" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "invoice" ADD CONSTRAINT "vendor_invoice" FOREIGN KEY ("vendor_id") REFERENCES "vendor" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "invoice" ADD CONSTRAINT "work_order_invoice" FOREIGN KEY ("work_order_id") REFERENCES "work_orders" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "ticket" ADD CONSTRAINT "ticket_invoice" FOREIGN KEY ("invoice_id") REFERENCES "invoice" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "line_item" ADD CONSTRAINT "invoice_line_items" FOREIGN KEY ("invoice_id") REFERENCES "invoice" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "invoice" ADD CONSTRAINT "invoice_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "invoice" ADD CONSTRAINT "invoice_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "line_item" ADD CONSTRAINT "line_item_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "line_item" ADD CONSTRAINT "line_item_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "user" ADD CONSTRAINT "user_address" FOREIGN KEY ("address_id") REFERENCES "address" ("id") DEFERRABLE INITIALLY IMMEDIATE;;

ALTER TABLE "client_user" ADD CONSTRAINT "client_client_user" FOREIGN KEY ("client_id") REFERENCES "client" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "vendor_user" ADD CONSTRAINT "vendor_vendor_user" FOREIGN KEY ("vendor_id") REFERENCES "vendor" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "client_user" ADD CONSTRAINT "client_user_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "client_user" ADD CONSTRAINT "client_user_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "vendor_user" ADD CONSTRAINT "vendor_user_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "vendor_user" ADD CONSTRAINT "vendor_user_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "sessions" ADD CONSTRAINT "user_active" FOREIGN KEY ("user_id") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "notification" ADD CONSTRAINT "user_notification" FOREIGN KEY ("recipient") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "contractors" ADD CONSTRAINT "user_contractor" FOREIGN KEY ("user_id") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "vendor_user" ADD CONSTRAINT "user_vendor" FOREIGN KEY ("user_id") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "client_user" ADD CONSTRAINT "user_client" FOREIGN KEY ("user_id") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "sessions" ADD CONSTRAINT "sessions_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "sessions" ADD CONSTRAINT "sessions_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "notification" ADD CONSTRAINT "notification_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "notification" ADD CONSTRAINT "notification_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "well" ADD CONSTRAINT "client_wells" FOREIGN KEY ("client_id") REFERENCES "client" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "well_location" ADD CONSTRAINT "well_location_link" FOREIGN KEY ("well_id") REFERENCES "well" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "work_orders" ADD CONSTRAINT "work_order_well" FOREIGN KEY ("well_id") REFERENCES "well" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "vendor_well" ADD CONSTRAINT "vendor_well_vendor" FOREIGN KEY ("vendor_id") REFERENCES "vendor" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "vendor_well" ADD CONSTRAINT "vendor_well_well" FOREIGN KEY ("well_id") REFERENCES "well" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "well" ADD CONSTRAINT "well_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "well" ADD CONSTRAINT "well_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "well_location" ADD CONSTRAINT "well_location_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "well_location" ADD CONSTRAINT "well_location_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "vendor_well" ADD CONSTRAINT "vendor_well_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "vendor_well" ADD CONSTRAINT "vendor_well_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "vendor_services" ADD CONSTRAINT "vendor_services_vendor" FOREIGN KEY ("vendor_id") REFERENCES "vendor" ("id") DEFERRABLE INITIALLY IMMEDIATE;;

ALTER TABLE "vendor_services" ADD CONSTRAINT "vendor_services_service" FOREIGN KEY ("service_id") REFERENCES "services" ("id") DEFERRABLE INITIALLY IMMEDIATE;;

ALTER TABLE "services" ADD CONSTRAINT "services_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "services" ADD CONSTRAINT "services_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "vendor_services" ADD CONSTRAINT "vendor_services_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "vendor_services" ADD CONSTRAINT "vendor_services_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fraud_alerts" ADD CONSTRAINT "work_order_fraud" FOREIGN KEY ("work_order_id") REFERENCES "work_orders" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fraud_alerts" ADD CONSTRAINT "ticket_fraud" FOREIGN KEY ("ticket_id") REFERENCES "ticket" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fraud_alerts" ADD CONSTRAINT "fraud_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fraud_alerts" ADD CONSTRAINT "fraud_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "messages" ADD CONSTRAINT "chat_messages" FOREIGN KEY ("chat_id") REFERENCES "chat" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "messages" ADD CONSTRAINT "sender_message" FOREIGN KEY ("sender") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "messages" ADD CONSTRAINT "recipient_message" FOREIGN KEY ("recipient") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "chat" ADD CONSTRAINT "chat_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "chat" ADD CONSTRAINT "chat_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "messages" ADD CONSTRAINT "message_created_by" FOREIGN KEY ("created_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "messages" ADD CONSTRAINT "message_updated_by" FOREIGN KEY ("updated_by") REFERENCES "user" ("id") DEFERRABLE INITIALLY IMMEDIATE;