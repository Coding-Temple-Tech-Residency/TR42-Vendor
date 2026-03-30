from app.extensions import db


class VendorUser(db.Model):
    __tablename__ = "vendor_user"

    id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String, nullable=False)
    vendor_id = db.Column(db.String)
    role = db.Column(db.String)  # or Enum if you mapped core.role_options
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    created_by = db.Column(db.String, nullable=False)
    updated_by = db.Column(db.String, nullable=False)
