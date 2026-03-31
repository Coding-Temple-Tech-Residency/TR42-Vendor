from sqlalchemy import JSON

from . import db
from datetime import datetime

# User Model
class User(db.Model):
    __tablename__ = 'user'
    
    user_id = db.Column(db.String(20), primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    password_hash = db.Column(db.String(400), nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    user_type = db.Column(db.String(20), nullable=False)  # 'admin' or 'user'
    is_active = db.Column(db.Boolean, default=True)
    is_admin = db.Column(db.Boolean, default=False)
    profile_photo = db.Column(db.String(200), nullable=True)  # URL or file path to the profile photo   
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by = db.Column(db.String(20), nullable=False)
    updated_by = db.Column(db.String(20), nullable=False)
    
#  Association Table for Vendor and User
class VendorUser(db.Model):
    __tablename__ = 'vendor_user'
    
    vendor_user_id = db.Column(db.String(20), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    vendor_id = db.Column(db.String(20), db.ForeignKey('vendor.vendor_id'), nullable=False)
    role_id = db.Column(db.String(20), db.ForeignKey('role.role_id'), nullable=False)
    
    created_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    updated_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)

    
#  Association Table for Client and User
#class ClientUser(db.Model):
    #__tablename__ = 'client_user'
    
    #client_user_id = db.Column(db.String(20), primary_key=True)
    #client_role_id = db.Column(db.String(20), db.ForeignKey('client_role.client_role_id'), nullable=False)
    #user_id = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    #created_at = db.Column(db.DateTime, default=datetime.utcnow)
    #updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    #created_by = db.Column(db.String(80), db.ForeignKey('user.user_id'), nullable=False)
    #updated_by = db.Column(db.String(80), db.ForeignKey('user.user_id'), nullable=False)
    
    
# Association Table for Vendor and Service
class VendorService(db.Model):
    __tablename__ = 'vendor_service'
    
    vendor_service_id = db.Column(db.String(20), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    vendor_id = db.Column(db.String(20), db.ForeignKey('vendor.vendor_id'), nullable=False)
    service_id = db.Column(db.String(20), db.ForeignKey('services.service_id'), nullable=False)
    created_by = db.Column(db.String(80), db.ForeignKey('user.user_id'), nullable=False)
    updated_by = db.Column(db.String(80), db.ForeignKey('user.user_id'), nullable=False)
    
    
# Association Table for Vendor and Well
class VendorWell(db.Model):
    __tablename__ = 'vendor_well'
    
    vendor_well_id = db.Column(db.String(20), primary_key=True)
    vendor_id = db.Column(db.String(20), db.ForeignKey('vendor.vendor_id'), nullable=False)
    well_id = db.Column(db.String(20), db.ForeignKey('well.well_id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    created_by = db.Column(db.String(80), db.ForeignKey('user.user_id'), nullable=False)
    updated_by = db.Column(db.String(80), db.ForeignKey('user.user_id'), nullable=False)
    
    
# Vendor Model
class Vendor(db.Model):
    __tablename__ = 'vendor'
    
    vendor_id = db.Column(db.String(20), primary_key=True)
    company_name = db.Column(db.String(80), nullable=False)
    company_code = db.Column(db.String(20), unique=True, nullable=False)
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    end_date = db.Column(db.DateTime, nullable=True)
    primary_contact_name = db.Column(db.String(80), nullable=False)
    contact_email = db.Column(db.String(40), nullable=False)
    contact_phone = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False)  # 'active' or 'inactive'
    vendor_code = db.Column(db.String(20), nullable=False)  # 'active' or 'inactive'
    onboarding = db.Column(db.Boolean, nullable=False)
    compliance_status = db.Column(db.String(20), nullable=False)  # 'compliant' or 'non-compliant'
    description = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by = db.Column(db.String(80), nullable=False)
    updated_by = db.Column(db.String(80), nullable=False)
    address_id = db.Column(db.String(200), nullable=False)
    
    
# Client Model
#class Client(db.Model):
    #__tablename__ = 'client'
    
    #client_id = db.Column(db.Integer, primary_key=True)
    #client_company_name = db.Column(db.String(80), nullable=False)
    #start_date = db.Column(db.DateTime, default=datetime.utcnow)
    #end_date = db.Column(db.DateTime, nullable=True)
    #client_status = db.Column(db.String(20), nullable=False)  # 'active' or 'inactive'
    #client_code = db.Column(db.String(20), unique=True, nullable=False)
    
    
# Company Model
#class Company(db.Model):
    # __tablename__ = 'company'
    
    #company_id = db.Column(db.String(20), primary_key=True)
    #contractor_company_name = db.Column(db.String(80), nullable=False)
    #company_code = db.Column(db.String(20), nullable=False)
    #primary_contact_name = db.Column(db.String(80), nullable=False)
    #contact_email = db.Column(db.String(40), nullable=False)
    #contact_phone = db.Column(db.String(20), nullable=False)
    #street_address = db.Column(db.String(120), nullable=False)
    #city = db.Column(db.String(50), nullable=False)
    #state = db.Column(db.String(20), nullable=False)
    #zip_code = db.Column(db.Integer, nullable=False)
    
    
# Well Model
class Well(db.Model):
    __tablename__ = 'well'
    
    well_id = db.Column(db.String(20), primary_key=True)
    api_number = db.Column(db.String(20), unique=True, nullable=False)
    well_name = db.Column(db.String(80), nullable=False)
    operator = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False)  # 'active' or 'inactive' or 'drilling' or 'completed' or 'suspunded' or 'plugged' or 'abandoned'
    type = db.Column(db.String(20), nullable=False)  # 'oil', 'gas', or 'dry' or 'Injection' or 'Water Disposal' or 'Observation' or 'Oil & Gas'
    range = db.Column(db.String(2), nullable=False)  
    quarter = db.Column(db.String(2), nullable=False)
    ground_elevation = db.Column(db.Float, nullable=False) #?? ask later if it should be a float or an integer 
    total_depth = db.Column(db.Float, nullable=False) #?? ask later if it should be a float or an integer
    geofence_radius = db.Column(db.Float, nullable=False) #?? ask later if it should be a float or an integer
    spud_date = db.Column(db.DateTime, nullable=False)
    completion_date = db.Column(db.DateTime, nullable=True)
    access_instructions = db.Column(db.String(200), nullable=True)
    safety_notes = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    created_by = db.Column(db.String(80), db.ForeignKey('user.user_id'), nullable=False)
    updated_by = db.Column(db.String(80), db.ForeignKey('user.user_id'), nullable=False)
    
    
# Well Location Model
class WellLocation(db.Model):
    __tablename__ = 'well_location'
    
    well_location_id = db.Column(db.String(20), primary_key=True)
    surface_latitude = db.Column(db.Float, nullable=False)
    surface_longitude = db.Column(db.Float, nullable=False)
    bottom_latitude = db.Column(db.Float, nullable=False)
    bottom_longitude = db.Column(db.Float, nullable=False)
    county = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    field_name = db.Column(db.String(80), nullable=False)
    section = db.Column(db.Integer, nullable=False)
    township = db.Column(db.String(2), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    created_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    updated_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    well_id = db.Column(db.String(20), db.ForeignKey('well.well_id'), nullable=False)
    
    
# Contractor Model
class Contractor(db.Model):
    __tablename__ = 'contractors'
    
    contractor_id = db.Column(db.String(20), primary_key=True, nullable=False)
    employee_number = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    middle_name = db.Column(db.String(80), nullable=True)
    contact_number = db.Column(db.String(20), nullable=False)
    alternate_contact_number = db.Column(db.String(20), nullable=True)
    date_of_birth = db.Column(db.DateTime, nullable=False)
    ssn_last_four = db.Column(db.String(4), nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    contractor_status = db.Column(db.String(20), nullable=False)  # 'active' or 'inactive'
    biometric_enrolled = db.Column(db.Boolean, default=False)
    is_onboarded = db.Column(db.Boolean, default=False)
    is_subcontractor = db.Column(db.Boolean, default=False)
    is_fte = db.Column(db.Boolean, default=False)
    is_licensed = db.Column(db.Boolean, default=False)
    is_insured = db.Column(db.Boolean, default=False)
    is_certified = db.Column(db.Boolean, default=False)
    average_rating = db.Column(db.Float, nullable=True)
    years_of_experience = db.Column(db.Float, nullable=True)
    preferred_job_types = db.Column(JSON)  #using JSON type to store a list of preferred job types (e.g., ['drilling', 'maintenance'])
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    background_check_id = db.Column(db.String(20), nullable=True)
    drug_test_id = db.Column(db.String(20), db.ForeignKey('drug_test.drug_test_id'), nullable=True)
    vendor_id = db.Column(db.String(20), db.ForeignKey('vendor.vendor_id'), nullable=False)
    role_id = db.Column(db.String(20), db.ForeignKey('role.role_id'), nullable=False)# under vendor_manager_id in erd but no reference to vendor manager in the erd, so I added vendor role id instead
    address_id = db.Column(db.String(200), db.ForeignKey('address.address_id'), nullable=False)
    role = db.relationship('ContractorRole', backref='contractor')
    company = db.relationship('Company', backref='contractor')
    vendor = db.relationship('Vendor', backref='contractor')
    
    
# All roles under one model
class Role(db.Model):
    __tablename__ = 'role'
    
    role_id = db.Column(db.String(20), primary_key=True)
    role_name = db.Column(db.String(20), nullable=False)  # 'admin', 'manager', 'employee', etc.
    description = db.Column(db.String(200), nullable=True)
    role_options = db.Column(JSON, nullable=True)  # Store additional options or permissions as JSON
    
    
# Session Model
class Session(db.Model):
    __tablename__ = 'session'
    
    session_id = db.Column(db.String(20), primary_key=True)
    last_active = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    user_agent = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user = db.relationship('User', backref='session')
    user_id = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    created_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    updated_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    
# Service Model
class Service(db.Model):
    __tablename__ = 'services'
    
    service_id = db.Column(db.String(20), primary_key=True)
    service_name = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    created_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    updated_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    
# Ticket Model
class Ticket(db.Model):
    __tablename__ = 'ticket'
    
    ticket_id = db.Column(db.String(50), primary_key=True)
    description = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(20), nullable=False)  # 'open', 'in_progress', 'closed', etc.
    priority = db.Column(db.String(20), nullable=False)  # 'low', 'medium', 'high'
    start_date = db.Column(db.DateTime, nullable=True)
    due_date = db.Column(db.DateTime, nullable=True)
    estimated_duration = db.Column(db.Float, nullable=True)
    notes = db.Column(db.String(200), nullable=True)
    contractor_start_location = db.Column(db.String(100), nullable=True)
    contractor_end_location = db.Column(db.String(100), nullable=True)
    estimated_quantity = db.Column(db.Float, nullable=True)
    unit = db.Column(db.String(20), nullable=True)  # 'hours', 'tons', 'barrels', etc.
    special_requirements = db.Column(db.String(200), nullable=True)
    anomaly_flag = db.Column(db.Boolean, default=False)
    anomaly_reason = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    assigned_contractor_id = db.Column(db.String(20), db.ForeignKey('contractors.contractor_id'), nullable=True)
    vendor_id = db.Column(db.String(20), db.ForeignKey('vendor.vendor_id'), nullable=True)
    work_order_id = db.Column(db.String(50), db.ForeignKey('work_orders.work_order_id'), nullable=True)
    created_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    updated_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)

    
# Ticket Photos Model
class TicketPhoto(db.Model):
    __tablename__ = 'ticket_photos'
    
    photo_id = db.Column(db.String(50), primary_key=True)
    photo_content = db.Column(db.String(200), nullable=False)  # URL or file path to the photo
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    ticket_id = db.Column(db.String(50), db.ForeignKey('ticket.ticket_id'), nullable=False)
    ticket = db.relationship('Ticket', backref='photos')
    created_by = db.Column(db.String(80), db.ForeignKey('user.user_id'), nullable=False)
    updated_by = db.Column(db.String(80), db.ForeignKey('user.user_id'), nullable=False)
    uploaded_by = db.Column(db.String(80), db.ForeignKey('user.user_id'), nullable=False)
    
# Work Order Model
class WorkOrder(db.Model):
    __tablename__ = 'work_orders'
    
    work_order_id = db.Column(db.String(50), primary_key=True)
    assigned_at = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.String(200), nullable=False)
    current_status = db.Column(db.String(20), nullable=False)  # 'open', 'in_progress', 'closed', etc.
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime, nullable=True)
    due_date = db.Column(db.DateTime, nullable=True)
    comments = db.Column(db.String(200), nullable=True)
    location = db.Column(db.String(100), nullable=True)
    estimated_cost = db.Column(db.Float, nullable=True)
    estimated_duration = db.Column(db.Float, nullable=True)  # in hours
    priority = db.Column(db.String(20), nullable=False)  # 'low', 'medium', 'high'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    assigned_vendor_id = db.Column(db.String(20), db.ForeignKey('vendor.vendor_id'), nullable=True)
    well_id = db.Column(db.String(20), db.ForeignKey('well.well_id'), nullable=True)
    created_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    updated_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    
    
# Cancelled Work Order Model
class CancelledWorkOrder(db.Model):
    __tablename__ = 'cancelled_work_orders'
    
    id = db.Column(db.String(50), primary_key=True)
    work_order_id = db.Column(db.String(50), db.ForeignKey('work_orders.work_order_id'), nullable=False)
    cancellation_reason = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    work_order = db.relationship('WorkOrder', backref='cancelled_work_order')
    vendor_id = db.Column(db.String(20), db.ForeignKey('vendor.vendor_id'), nullable=False)
    created_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    updated_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    
    
# Fraud Alert Model
class FraudAlert(db.Model):
    __tablename__ = 'fraud_alerts'
    
    fraud_alerts_id = db.Column(db.String(50), primary_key=True)
    ticket_id = db.Column(db.String(50), nullable=False)
    severity = db.Column(db.String(20), nullable=False)  # 'low', 'medium', 'high'
    description = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(20), nullable=False)  # 'open', 'in_progress', 'closed', etc.
    flagged_at = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    work_order_id = db.Column(db.String(50), db.ForeignKey('work_orders.work_order_id'), nullable=False)
    work_order = db.relationship('WorkOrder', backref='fraud_alert')
    created_by = db.Column(db.String(80), db.ForeignKey('user.user_id'), nullable=False)
    updated_by = db.Column(db.String(80), db.ForeignKey('user.user_id'), nullable=False)
    
    
# Certifications Model
class Certification(db.Model):
    __tablename__ = 'certifications'
    
    certification_id = db.Column(db.String(50), primary_key=True)
    certification_name = db.Column(db.String(80), nullable=False)
    certifying_body = db.Column(db.String(80), nullable=False)
    certification_number = db.Column(db.Integer, nullable=False)
    issue_date = db.Column(db.DateTime, nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)
    certification_document_url = db.Column(db.String(200), nullable=True)
    certification_verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_by = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    created_by = db.Column(db.String(80), db.ForeignKey('user.user_id'), nullable=False)
    updated_by = db.Column(db.String(80), db.ForeignKey('user.user_id'), nullable=False)
    contractor_id = db.Column(db.String(20), db.ForeignKey('contractors.contractor_id'), nullable=False)
    
    
# MSA Model
class Msa(db.Model):
    __tablename__ = 'msa'
    
    msa_id = db.Column(db.String(20), primary_key=True)
    version = db.Column(db.String(20), nullable=False)
    effective_date = db.Column(db.DateTime, nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False)  # 'active' or 'inactive'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    vendor_id = db.Column(db.String(20), db.ForeignKey('vendor.vendor_id'), nullable=False)
    created_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    updated_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    
# MSA Model
class MsaRequirement(db.Model):
    __tablename__ = 'msa_requirements'
    
    id = db.Column(db.String(20), primary_key=True)
    msa_id = db.Column(db.String(20), primary_key=True)
    category = db.Column(db.String(20), nullable=False)  # 'insurance', 'compliance', 'safety', etc.
    rule_type = db.Column(db.String(20), nullable=False)  # 'document_expiration', 'compliance_status', etc.
    decription = db.Column(db.String(200), nullable=True)
    value = db.Column(db.String(20), nullable=False)  # e.g., 'expired', 'non-compliant', etc.
    unit = db.Column(db.String(20), nullable=True)  # e.g., 'days', 'months', etc. (if applicable)
    source_field_id = db.Column(db.String(50), nullable=True)  # e.g., 'insurance.expiration_date', 'compliance.compliance_status', etc.
    page_number = db.Column(db.Integer, nullable=True)  # If the requirement is based on a specific page in the MSA document
    extracted_text = db.Column(db.String(200), nullable=True)  # Store the extracted text that was used to evaluate the requirement
    confidence_score = db.Column(db.Float, nullable=True)  # Store the confidence score of the extracted text (if applicable)
    extra_data = db.Column(JSON, nullable=True)  # Store any additional metadata related to the requirement evaluation
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    created_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    updated_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    
# Compliance Document Model
class ComplianceDocument(db.Model):
    __tablename__ = 'compliance_document'
    
    compliance_id = db.Column(db.String(20), primary_key=True)
    compliance_document = db.Column(db.String(200), nullable=False)  # URL or file path to the compliance document
    compliance_status = db.Column(db.Boolean, default=False)  # True if compliant, False if non-compliant
    expiration_date = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 
    
    vendor_id = db.Column(db.String(20), db.ForeignKey('vendor.vendor_id'), nullable=False)
    created_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    updated_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    
# Insurance Model
class Insurance(db.Model):
    __tablename__ = 'insurance'
    
    insurance_id = db.Column(db.String(50), primary_key=True)
    insurance_type = db.Column(db.String(20), nullable=False)  # 'general_liability', 'workers_compensation', etc.
    provider_name = db.Column(db.String(80), nullable=False)
    policy_number = db.Column(db.String(50), nullable=False)
    provide_phone = db.Column(db.String(11), nullable=False)
    coverage_amount = db.Column(db.Float, nullable=False)
    deductible = db.Column(db.Float, nullable=False)
    issue_date = db.Column(db.DateTime, nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)
    insurance_document_url = db.Column(db.String(200), nullable=True)
    insurance_verified = db.Column(db.Boolean, default=False)
    additional_insurance_url = db.Column(db.String(200), nullable=True)
    additional_insured_certificate_url = db.Column(db.String(200), nullable=True)
    
    created_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    updated_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    contractor_id = db.Column(db.String(20), db.ForeignKey('contractors.contractor_id'), nullable=False)
    
    
# License Model
class License(db.Model):
    __tablename__ = 'licenses'
    
    license_id = db.Column(db.String(50), primary_key=True)
    license_type = db.Column(db.String(20), nullable=False)  # 'drilling', 'transportation', etc.
    license_state = db.Column(db.String(20), nullable=False)
    license_number = db.Column(db.String(50), nullable=False)
    license_expiration_date = db.Column(db.DateTime, nullable=False)
    license_document_url = db.Column(db.String(200), nullable=True)
    license_verified = db.Column(db.Boolean, default=False)
    license_verified_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    licensed_verified_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    created_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    updated_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    contractor_id = db.Column(db.String(20), db.ForeignKey('contractors.contractor_id'), nullable=False)
    
    
# Invoice Model
class Invoice(db.Model):
    __tablename__ = 'invoice'
    
    invoice_id = db.Column(db.String(50), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    invoice_date = db.Column(db.DateTime, nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    period_start = db.Column(db.DateTime, nullable=False)
    period_end = db.Column(db.DateTime, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    invoice_status = db.Column(db.String(20), nullable=False)  # 'draft', 'sent', 'paid', 'overdue', etc.
    updated_by = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    vendor_id = db.Column(db.String(20), db.ForeignKey('vendor.vendor_id'), nullable=False)
    work_order_id = db.Column(db.String(20), db.ForeignKey('work_orders.work_order_id'), nullable=False)
    ticket_id = db.Column(db.String(20), db.ForeignKey('ticket.ticket_id'), nullable=False)
    created_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    updated_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    
# Line Item Model
class LineItem(db.Model):
    __tablename__ = 'line_item'
    
    line_item_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    rate = db.Column(db.Float, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    invoice_id = db.Column(db.String(50), db.ForeignKey('invoice.invoice_id'), nullable=False)
    created_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    updated_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    
# Messages Model
class Message(db.Model):
    __tablename__ = 'messages'
    
    message_id = db.Column(db.String(20), primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    chat_id = db.Column(db.String(20), db.ForeignKey('chat.chat_id'), nullable=False)
    sender_id = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    recipient_id = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    chat = db.relationship('Chat', backref='messages')
    sender = db.relationship('User', foreign_keys=[sender_id], backref='sent_messages')
    recipient = db.relationship('User', foreign_keys=[recipient_id], backref='received_messages')
    created_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    updated_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    
    
# Chat Model
class Chat(db.Model):
    __tablename__ = 'chat'
    
    chat_id = db.Column(db.String(20), primary_key=True)
    messages = db.relationship('Message', backref='chat')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    created_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    updated_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    
    
# Notification Model
class Notification(db.Model):
    __tablename__ = 'notification'
    
    notification_id = db.Column(db.String(20), primary_key=True)
    level = db.Column(db.String(20), nullable=False)  # 'info', 'warning', 'critical', etc.
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    message = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    recipient_id = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    recipient = db.relationship('User', foreign_keys=[recipient_id], backref='notifications')
    created_by = db.Column(db.String(80), db.ForeignKey('user.user_id'), nullable=False)
    updated_by = db.Column(db.String(80), db.ForeignKey('user.user_id'), nullable=False)
    
    
# Job Model
#class Job(db.Model):
    #__tablename__ = 'job'
    
    #job_id = db.Column(db.String(50), primary_key=True)
    #description = db.Column(db.String(200), nullable=True)
    #priority = db.Column(db.String(20), nullable=False)  # 'low', 'medium', 'high'
    #job_status = db.Column(db.String(20), nullable=False)  # 'open', 'in_progress', 'closed', etc.
    #estimated_duration = db.Column(db.Float, nullable=True)  # in hours
    #start_time = db.Column(db.DateTime, nullable=True)
    #end_time = db.Column(db.DateTime, nullable=True)
    #estimated_quantity = db.Column(db.Float, nullable=True)
    #unit = db.Column(db.String(20), nullable=True)  # 'hours', 'tons', 'barrels', etc.
    #notes = db.Column(db.String(200), nullable=True)  
    #special_requirements = db.Column(db.String(200), nullable=True)
    #contractor_start_location = db.Column(db.String(100), nullable=True)
    #contractor_end_location = db.Column(db.String(100), nullable=True)
    #anomaly_flag = db.Column(db.Boolean, default=False)
    #anomaly_reason = db.Column(db.String(200), nullable=True)
    
    #work_order_id = db.Column(db.String(50), db.ForeignKey('work_order.work_order_id'), nullable=False)
    #assigned_contractor_id = db.Column(db.Integer, db.ForeignKey('contractor.contractor_id'), nullable=True)
    
    
# Ratings Model
class Rating(db.Model):
    __tablename__ = 'ratings'
    
    rating_id = db.Column(db.String(20), primary_key=True)
    rating_value = db.Column(db.Float, nullable=False)  # e.g., 1.0 to 5.0
    comments = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    contractor_id = db.Column(db.String(20), db.ForeignKey('contractors.contractor_id'), nullable=False)
    ticket_id = db.Column(db.String(50), db.ForeignKey('ticket.ticket_id'), nullable=False)
    created_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    updated_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)

# Background Check Model
class BackgroundCheck(db.Model):
    __tablename__ = 'background_check'
    
    background_check_id = db.Column(db.String(20), primary_key=True)
    background_check_passed = db.Column(db.Boolean, default=False)
    background_check_date = db.Column(db.DateTime, nullable=True)
    background_check_provider = db.Column(db.String(80), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    contractor_id = db.Column(db.String(20), db.ForeignKey('contractors.contractor_id'), nullable=False)
    created_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    updated_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)


#Drug Test Model
class DrugTest(db.Model):
    __tablename__ = 'drug_test'
    
    drug_test_id = db.Column(db.String(20), primary_key=True)
    drug_test_passed = db.Column(db.Boolean, default=False)
    drug_test_date = db.Column(db.DateTime, nullable=True)
    drug_test_provider = db.Column(db.String(80), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    contractor_id = db.Column(db.String(20), db.ForeignKey('contractors.contractor_id'), nullable=False)
    created_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    updated_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)


# Address Model
class Address(db.Model):
    __tablename__ = 'address'
    
    address_id = db.Column(db. String(20), primary_key=True)
    street = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(20), nullable=False)
    zip = db.Column(db.Integer, nullable=False)
    country = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)
    updated_by = db.Column(db.String(20), db.ForeignKey('user.user_id'), nullable=False)