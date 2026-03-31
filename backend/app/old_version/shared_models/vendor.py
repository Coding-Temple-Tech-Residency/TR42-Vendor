# from app.extensions import db
# from datetime import datetime

# class Vendor(db.Model):
#     __tablename__ = 'vendor'
    
#     vendor_id = db.Column(db.Integer, primary_key=True)
#     company_name = db.Column(db.String(80), nullable=False)
#     start_date = db.Column(db.DateTime, default=datetime.utcnow)
#     end_date = db.Column(db.DateTime, nullable=True)
#     vendor_status = db.Column(db.String(20), nullable=False)
#     vendor_code = db.Column(db.String(20), unique=True, nullable=False)
#     onboarding = db.Column(db.String(20), nullable=False)
#     compliance_status = db.Column(db.String(20), nullable=False)