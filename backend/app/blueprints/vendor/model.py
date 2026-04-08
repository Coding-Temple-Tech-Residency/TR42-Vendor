from app.extensions import db
from app.functions import generate_uuid

from sqlalchemy import (
    Boolean,
    Enum,
    String,
    ForeignKey,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship


import enum


class VendorStatus(enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class ComplianceStatus(enum.Enum):
    EXPIRED = "expired"
    INCOMPLETE = "incomplete"
    COMPLETE = "complete"


class Vendor(db.Model):
    __tablename__ = "vendor"

    vendor_id: Mapped[str] = mapped_column(
        String(36), primary_key=True, nullable=False, default=generate_uuid
    )

    company_name: Mapped[str] = mapped_column(String(80), nullable=False, unique=True)

    company_code: Mapped[str] = mapped_column(String, nullable=True)

    primary_contact_name: Mapped[str] = mapped_column(String)

    company_email: Mapped[str] = mapped_column(String, nullable=False)
    company_phone: Mapped[str] = mapped_column(String, nullable=False)

    service_type: Mapped[str] = mapped_column(String, nullable=False)

    status: Mapped[VendorStatus] = mapped_column(
        Enum(VendorStatus, name="vendor_status"),
        nullable=False,
        default=VendorStatus.ACTIVE,
    )

    onboarding: Mapped[bool] = mapped_column(Boolean, nullable=True, default=False)

    compliance_status: Mapped[ComplianceStatus] = mapped_column(
        Enum(ComplianceStatus, name="compliance_status"),
        nullable=False,
        default=ComplianceStatus.INCOMPLETE,
    )

    description: Mapped[str] = mapped_column(String, nullable=True)

    address_id: Mapped[str] = mapped_column(
        ForeignKey("address.address_id"),
        unique=True,
    )

    # relationships

    address: Mapped["Address"] = relationship(back_populates="vendor")

    vendor_links: Mapped[list["VendorUser"]] = relationship(
        back_populates="vendor", cascade="all, delete-orphan"
    )
