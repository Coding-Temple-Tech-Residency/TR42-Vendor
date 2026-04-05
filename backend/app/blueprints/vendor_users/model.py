from app.extensions import db
from datetime import datetime
from uuid import uuid4


class VendorUser(db.Model):
    __tablename__ = "vendor_user"

    #id = db.Column(db.String(36), primary_key=True)
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))

    user_id = db.Column(db.String(36), db.ForeignKey("user.user_id"), nullable=False)
    vendor_id = db.Column(db.String(36), db.ForeignKey("vendor.vendor_id"), nullable=False)

    role = db.Column(
        db.Enum("admin", "user", "operator", "vendor", "contractor", name="role_options"),
        nullable=False
    )

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by = db.Column(db.String(36), db.ForeignKey("user.user_id"), nullable=False)
    updated_by = db.Column(db.String(36), db.ForeignKey("user.user_id"))


    

    # Relationships
    user = db.relationship("User", back_populates="vendor_links",foreign_keys=[user_id])
    vendor = db.relationship("Vendor", back_populates="users")