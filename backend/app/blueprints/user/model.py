from app.extensions import db
from datetime import datetime
from uuid import uuid4

class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    username = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(400), nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)

    type = db.Column(
        db.Enum("operator", "vendor", "contractor", name="user_type"),
        nullable=False
    )

    is_active = db.Column(db.Boolean, default=True, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    profile_photo = db.Column(db.LargeBinary)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    created_by = db.Column(db.String(36), nullable=False)
    updated_by = db.Column(db.String(36))

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)


    # Relationship to vendor_user join table
    vendor_links = db.relationship("VendorUser", back_populates="user",foreign_keys="VendorUser.user_id")