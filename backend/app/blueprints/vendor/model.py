from app.extensions import db
from app.functions import generate_uuid
from datetime import date
from typing import List
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, Date, Float, ForeignKey, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Vendor(db.Model):
    __tablename__ = "vendor"

    vendor_id: Mapped[str] = mapped_column(
        String(36), unique=True, nullable=False, default=generate_uuid
    )

    company_name: Mapped[str] = mapped_column(String(80), nullable=False, unique=True)

    company_code: Mapped[str] = mapped_column(String)

    primary_contact_name: Mapped[str] = mapped_column(String)
    company_email = db.Column(db.String, nullable=False)
    company_phone = db.Column(db.String, nullable=False)

    status = db.Column(
        db.Enum("active", "inactive", name="vendor_status"), nullable=False
    )

    onboarding = db.Column(db.Boolean, nullable=False)

    compliance_status = db.Column(
        db.Enum("expired", "incomplete", "complete", name="compliance_status")
    )

    # description = db.Column(db.Text)

    address_id = db.Column(db.String, db.ForeignKey("address.address_id"))
    created_by = db.Column(db.String, default="system")
    updated_by = db.Column(db.String, default="system")

    # FIXED: use back_populates instead of backref
    address = db.relationship("Address", back_populates="vendor")

    users = db.relationship("VendorUser", back_populates="vendor")
