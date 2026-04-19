from datetime import datetime
from app.functions import generate_uuid, utc_now
from typing import TYPE_CHECKING
from sqlalchemy import (
    Boolean,
    DateTime,
    Enum,
    String,
    ForeignKey,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
import enum
from app.base import BaseModel


if TYPE_CHECKING:
    from app.blueprints.address.model import Address
    from app.blueprints.vendor_user.model import VendorUser
    from app.blueprints.vendor_contractor.model import VendorContractor
    from app.blueprints.compliance_document.model import ComplianceDocument
    from app.blueprints.invoices.model import Invoice
    from app.blueprints.vendor_service.model import VendorService
    from app.blueprints.work_orders.model import WorkOrder


class VendorStatus(enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class ComplianceStatus(enum.Enum):
    EXPIRED = "expired"
    INCOMPLETE = "incomplete"
    COMPLETE = "complete"


class Vendor(BaseModel):
    __tablename__ = "vendor"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, nullable=False, default=generate_uuid
    )

    company_name: Mapped[str] = mapped_column(String(80), nullable=False, unique=True)

    company_code: Mapped[str] = mapped_column(String, nullable=True)

    primary_contact_name: Mapped[str] = mapped_column(String)

    start_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=utc_now,
    )

    end_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=True,
    )

    company_email: Mapped[str] = mapped_column(String, nullable=False)
    company_phone: Mapped[str] = mapped_column(String, nullable=False)

    service_type: Mapped[str] = mapped_column(String, nullable=False)

    status: Mapped[VendorStatus] = mapped_column(
        Enum(VendorStatus, name="vendor_status"),
        nullable=False,
        default=VendorStatus.ACTIVE,
    )

    vendor_code: Mapped[str] = mapped_column(String, unique=True)

    onboarding: Mapped[bool] = mapped_column(Boolean, nullable=True, default=False)

    compliance_status: Mapped[ComplianceStatus] = mapped_column(
        Enum(ComplianceStatus, name="compliance_status"),
        nullable=False,
        default=ComplianceStatus.INCOMPLETE,
    )

    description: Mapped[str] = mapped_column(String, nullable=True)

    address_id: Mapped[str] = mapped_column(
        ForeignKey("address.id"),
        unique=True,
    )

    # Relationships
    address: Mapped["Address"] = relationship(
        "Address",
        back_populates="vendor",
        foreign_keys=[address_id],
    )

    user_links: Mapped[list["VendorUser"]] = relationship(
        "VendorUser", back_populates="vendor", cascade="all, delete-orphan"
    )

    contractor_links: Mapped[list["VendorContractor"]] = relationship(
        "VendorContractor",
        back_populates="vendor",
        foreign_keys="VendorContractor.vendor_id",
        cascade="all, delete-orphan",
    )

    compliance_documents: Mapped[list["ComplianceDocument"]] = relationship(
        "ComplianceDocument",
        back_populates="vendor",
        cascade="all, delete-orphan",
    )

    invoices: Mapped[list["Invoice"]] = relationship(
        "Invoice", back_populates="vendor", cascade="all, delete-orphan"
    )

    service_links: Mapped[list["VendorService"]] = relationship(
        "VendorService",
        back_populates="vendor",
        cascade="all, delete-orphan",
    )

    work_orders: Mapped[list["WorkOrder"]] = relationship(
        "WorkOrder",
        back_populates="vendor",
    )
