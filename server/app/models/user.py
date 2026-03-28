from . import db
from datetime import datetime

# User Model
class User(db.Model):
    __tablename__ = 'user'
    
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(400), nullable=False) # should this be hashed????
    email = db.Column(db.String(40), unique=True, nullable=False)
    type = db.Column(db.String(20), nullable=False)  # 'admin' or 'user'
    
#  Association Table for Vendor and User
class VendorUser(db.Model):
    __tablename__ = 'vendor_user'
    
    vendor_user_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.vendor_id'), nullable=False)
    vendor_role_id = db.Column(db.Integer, db.ForeignKey('vendor_role.vendor_role_id'), nullable=False)
    
#  Association Table for Client and User
class ClientUser(db.Model):
    __tablename__ = 'client_user'
    
    client_user_id = db.Column(db.Integer, primary_key=True)
    client_role_id = db.Column(db.Integer, db.ForeignKey('client_role.client_role_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    
    
# Association Table for Vendor and Service
class VendorService(db.Model):
    __tablename__ = 'vendor_service'
    
    vendor_service_id = db.Column(db.Integer, primary_key=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.vendor_id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.service_id'), nullable=False)
    
    
# Association Table for Vendor and Well
class VendorWell(db.Model):
    __tablename__ = 'vendor_well'
    
    vendor_well_id = db.Column(db.Integer, primary_key=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.vendor_id'), nullable=False)
    well_id = db.Column(db.Integer, db.ForeignKey('well.well_id'), nullable=False)
    
    
# Vendor Model
class Vendor(db.Model):
    __tablename__ = 'vendor'
    
    vendor_id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(80), nullable=False)
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    end_date = db.Column(db.DateTime, nullable=True)
    vendor_status = db.Column(db.String(20), nullable=False)  # 'active' or 'inactive'
    vendor_code = db.Column(db.String(20), unique=True, nullable=False)
    onboarding = db.Column(db.String(20), nullable=False)  # 'completed' or 'in-progress'
    compliance_status = db.Column(db.String(20), nullable=False)  # 'compliant' or 'non-compliant'
    
    
# Client Model
class Client(db.Model):
    __tablename__ = 'client'
    
    client_id = db.Column(db.Integer, primary_key=True)
    client_company_name = db.Column(db.String(80), nullable=False)
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    end_date = db.Column(db.DateTime, nullable=True)
    client_status = db.Column(db.String(20), nullable=False)  # 'active' or 'inactive'
    client_code = db.Column(db.String(20), unique=True, nullable=False)
    
    
# Company Model
class Company(db.Model):
    __tablename__ = 'company'
    
    company_id = db.Column(db.Integer, primary_key=True)
    contractor_company_name = db.Column(db.String(80), nullable=False)
    company_code = db.Column(db.String(20), nullable=False)
    primary_contact_name = db.Column(db.String(80), nullable=False)
    contact_email = db.Column(db.String(40), nullable=False)
    contact_phone = db.Column(db.String(20), nullable=False)
    street_address = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(20), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    
    
# Well Model
class Well(db.Model):
    __tablename__ = 'well'
    
    well_id = db.Column(db.Integer, primary_key=True)
    api_number = db.Column(db.String(20), unique=True, nullable=False)
    well_name = db.Column(db.String(80), nullable=False)
    operator = db.Column(db.String(80), nullable=False)
    well_status = db.Column(db.String(20), nullable=False)  # 'active' or 'inactive' or 'drilling' or 'completed' or 'suspunded' or 'plugged' or 'abandoned'
    type = db.Column(db.String(20), nullable=False)  # 'oil', 'gas', or 'dry' or 'Injection' or 'Water Disposal' or 'Observation' or 'Oil & Gas'
    range = db.Column(db.String(2), nullable=False)  
    quarter = db.Column(db.String(2), nullable=False)
    ground_elevation = db.Column(db.Float, nullable=False) #?? ask later if it should be a float or an integer 
    total_depth = db.Column(db.Float, nullable=False) #?? ask later if it should be a float or an integer
    geofence_radius = db.Column(db.Float, nullable=False) #?? ask later if it should be a float or an integer
    spud_date = db.Column(db.DateTime, nullable=False)
    completion_date = db.Column(db.DateTime, nullable=True)
    access_instructions = db.Column(db.String(200), nullable=True)
    
    company_id = db.Column(db.Integer, db.ForeignKey('company.company_id'), nullable=False)
    
    
# Well Location Model
class WellLocation(db.Model):
    __tablename__ = 'well_location'
    
    well_location_id = db.Column(db.Integer, primary_key=True)
    surface_latitude = db.Column(db.Float, nullable=False)
    surface_longitude = db.Column(db.Float, nullable=False)
    bottom_latitude = db.Column(db.Float, nullable=False)
    bottom_longitude = db.Column(db.Float, nullable=False)
    county = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    field_name = db.Column(db.String(80), nullable=False)
    section = db.Column(db.Integer, nullable=False)
    township = db.Column(db.String(2), nullable=False)
    
    well_id = db.Column(db.Integer, db.ForeignKey('well.well_id'), nullable=False)
    
    
# Contractor Model
class Contractor(db.Model):
    __tablename__ = 'contractor'
    
    contractor_id = db.Column(db.Integer, primary_key=True, nullable=False)
    employee_number = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    contact_number = db.Column(db.String(20), nullable=False)
    contractor_status = db.Column(db.String(20), nullable=False)  # 'active' or 'inactive'
    
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.vendor_id'), nullable=False)
    vendor_role_id = db.Column(db.Integer, db.ForeignKey('vendor_role.vendor_role_id'), nullable=False)# add vendor role model table
    Company_id = db.Column(db.Integer, db.ForeignKey('company.company_id'), nullable=False)
    contractor_role_id = db.Column(db.Integer, db.ForeignKey('contractor_role.contractor_role_id'), nullable=False) # Add contractor role model table
    
    role = db.relationship('ContractorRole', backref='contractor')
    company = db.relationship('Company', backref='contractor')
    vendor = db.relationship('Vendor', backref='contractor')
    
# Vendor Role Model
class VendorRole(db.Model):
    __tablename__ = 'vendor_role'
    
    vendor_role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(20), nullable=False)  # 'admin', 'manager', 'employee', etc.
    
    
# Client Role Model
class ClientRole(db.Model):
    __tablename__ = 'client_role'
    
    client_role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(20), nullable=False)  # 'admin', 'manager', 'employee', etc.
    
    
# Contractor Role Model
class ContractorRole(db.Model):
    __tablename__ = 'contractor_role'
    
    contractor_role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(20), nullable=False)  # 'admin', 'manager', 'employee', 'field technician', etc.
    
    
# Session Model
class Session(db.Model):
    __tablename__ = 'session'
    
    session_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    login_time = db.Column(db.DateTime, default=datetime.utcnow)
    logout_time = db.Column(db.DateTime, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    user_agent = db.Column(db.String(200), nullable=True)
    
    user = db.relationship('User', backref='session')
    
    
# Service Model
class Service(db.Model):
    __tablename__ = 'service'
    
    service_id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    
    
# Work Order Model
class WorkOrder(db.Model):
    __tablename__ = 'work_order'
    
    work_order_id = db.Column(db.String(50), primary_key=True)
    assigned_at = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), nullable=False)  # 'open', 'in_progress', 'closed', etc.
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime, nullable=True)
    due_date = db.Column(db.DateTime, nullable=True)
    comments = db.Column(db.String(200), nullable=True)
    location = db.Column(db.String(100), nullable=True)
    estimated_cost = db.Column(db.Float, nullable=True)
    estimated_duration = db.Column(db.Float, nullable=True)  # in hours
    priority = db.Column(db.String(20), nullable=False)  # 'low', 'medium', 'high'
    
    assigned_vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.vendor_id'), nullable=True)
    well_id = db.Column(db.Integer, db.ForeignKey('well.well_id'), nullable=True)
    
    
# Fraud Alert Model
class FraudAlert(db.Model):
    __tablename__ = 'fraud_alert'
    
    fraud_alert_id = db.Column(db.String(50), primary_key=True)
    alert_type = db.Column(db.String(20), nullable=False)  # 'suspicious_login', 'multiple_failed_logins', etc.
    description = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(20), nullable=False)  # 'active' or 'resolved'
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    work_order_id = db.Column(db.String(50), db.ForeignKey('work_order.work_order_id'), nullable=False)
    
    work_order = db.relationship('WorkOrder', backref='fraud_alert')
    
    
# Compliance Document Model
class ComplianceDocument(db.Model):
    __tablename__ = 'compliance_document'
    
    compliance_id = db.Column(db.String(50), primary_key=True)
    document_name = db.Column(db.String(80), nullable=False)
    document_type = db.Column(db.String(20), nullable=False)  # 'safety_certificate', 'insurance', etc.
    issue_date = db.Column(db.DateTime, nullable=False)
    expiry_date = db.Column(db.DateTime, nullable=False)
    compliance_status = db.Column(db.String(20), nullable=False)  # 'valid' or 'expired'
    
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.vendor_id'), nullable=False)
    
    
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
    
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.vendor_id'), nullable=False)
    work_order_id = db.Column(db.String(50), db.ForeignKey('work_order.work_order_id'), nullable=False)
    
    
# Line Item Model
class LineItem(db.Model):
    __tablename__ = 'line_item'
    
    line_item_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    rate = db.Column(db.Float, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    
    invoice_id = db.Column(db.String(50), db.ForeignKey('invoice.invoice_id'), nullable=False)
    
    
# Messages Model
class Message(db.Model):
    __tablename__ = 'message'
    
    message_id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    is_read = db.Column(db.Boolean, default=False)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.chat_id'), nullable=False)
    
    chat = db.relationship('Chat', backref='message')
    sender = db.relationship('User', foreign_keys=[sender_id], backref='sent_message')
    recipient = db.relationship('User', foreign_keys=[recipient_id], backref='received_message')
    
    
# Chat Model
class Chat(db.Model):
    __tablename__ = 'chat'
    
    chat_id = db.Column(db.Integer, primary_key=True)
    messages = db.relationship('Message', backref='chat')
    
    
# Job Model
class Job(db.Model):
    __tablename__ = 'job'
    
    job_id = db.Column(db.String(50), primary_key=True)
    description = db.Column(db.String(200), nullable=True)
    priority = db.Column(db.String(20), nullable=False)  # 'low', 'medium', 'high'
    job_status = db.Column(db.String(20), nullable=False)  # 'open', 'in_progress', 'closed', etc.
    estimated_duration = db.Column(db.Float, nullable=True)  # in hours
    start_time = db.Column(db.DateTime, nullable=True)
    end_time = db.Column(db.DateTime, nullable=True)
    estimated_quantity = db.Column(db.Float, nullable=True)
    unit = db.Column(db.String(20), nullable=True)  # 'hours', 'tons', 'barrels', etc.
    notes = db.Column(db.String(200), nullable=True)  
    special_requirements = db.Column(db.String(200), nullable=True)
    contractor_start_location = db.Column(db.String(100), nullable=True)
    contractor_end_location = db.Column(db.String(100), nullable=True)
    anomaly_flag = db.Column(db.Boolean, default=False)
    anomaly_reason = db.Column(db.String(200), nullable=True)
    
    work_order_id = db.Column(db.String(50), db.ForeignKey('work_order.work_order_id'), nullable=False)
    assigned_contractor_id = db.Column(db.Integer, db.ForeignKey('contractor.contractor_id'), nullable=True)
    
