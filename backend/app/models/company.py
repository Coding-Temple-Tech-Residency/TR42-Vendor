from app.extensions import db

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