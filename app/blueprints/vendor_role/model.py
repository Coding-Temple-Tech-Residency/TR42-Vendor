from app.extensions import db

class VendorRole(db.Model):
    __tablename__ = "vendor_role"

    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.Text)
