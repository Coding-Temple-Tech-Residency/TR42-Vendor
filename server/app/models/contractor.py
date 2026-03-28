from app.extensions import db

class Contractor(db.Model):
    __tablename__ = 'contractor'
    
    contractor_id = db.Column(db.Integer, primary_key=True)
    employee_number = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    contact_number = db.Column(db.String(20), nullable=False)
    contractor_status = db.Column(db.String(20), nullable=False)
    
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.vendor_id'))
    vendor_role_id = db.Column(db.Integer, db.ForeignKey('vendor_role.vendor_role_id'))
    company_id = db.Column(db.Integer, db.ForeignKey('company.company_id'))
    contractor_role_id = db.Column(db.Integer, db.ForeignKey('contractor_role.contractor_role_id'))

    role = db.relationship('ContractorRole', backref='contractors')
    company = db.relationship('Company', backref='contractors')
    vendor = db.relationship('Vendor', backref='contractors')