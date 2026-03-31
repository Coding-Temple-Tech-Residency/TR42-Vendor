from app.extensions import db


class VendorUser(db.Model):
    __tablename__ = "vendor_user"

    id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String, nullable=False)
    vendor_id = db.Column(db.String)
    role_id = db.Column(db.String,db.ForeignKey('role.role_id'))
    role = db.relationship('Role')
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    created_by = db.Column(db.String, nullable=False)
    updated_by = db.Column(db.String, nullable=False)
