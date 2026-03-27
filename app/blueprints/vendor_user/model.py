from app.extensions import db

class VendorUser(db.Model):
    __tablename__ = "vendor_user"

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    role_id = db.Column(db.Integer, nullable=False)
