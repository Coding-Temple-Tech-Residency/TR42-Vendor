from __future__ import annotations
from datetime import datetime
from uuid import uuid4
from app.extensions import db



class Address(db.Model):
    __tablename__ = "address"

    address_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    street = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String(20))
    zipcode = db.Column(db.String(10))
    country = db.Column(db.String(2))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by = db.Column(db.String, nullable=False)
    updated_by = db.Column(db.String)

    # FIXED: match back_populates
    vendor = db.relationship("Vendor", back_populates="address", uselist=False)