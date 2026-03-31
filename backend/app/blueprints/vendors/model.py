from __future__ import annotations

from datetime import datetime
from typing import Optional
import uuid
import enum

from app.shared_models.address import Address
from sqlalchemy import String, DateTime, Boolean, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions import db
from functions import utc_now


class ComplianceStatus(enum.Enum):
    EXPIRED = "expired"
    INCOMPLETE = "incomplete"
    COMPLETE = "complete"


class Vendor(db.Model):
    __tablename__ = "vendors"

    vendor_id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    company_name: Mapped[str] = mapped_column(String(80), nullable=False, unique=True)

    company_code: Mapped[Optional[str]] = mapped_column(String)

    company_email: Mapped[str] = mapped_column(String, nullable=False)
    company_phone: Mapped[str] = mapped_column(String, nullable=False)

    primary_contact_name: Mapped[Optional[str]] = mapped_column(String)

    address_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("addresses.address_id"), unique=True
    )
    address: Mapped[Optional["Address"]] = relationship(
        single_parent=True,
        back_populates="vendor",
        uselist=False,
        cascade="all, delete-orphan",
    )
    service_type: Mapped[Optional[str]] = mapped_column(String(100))
    status: Mapped[ComplianceStatus] = mapped_column(
        Enum(ComplianceStatus), default=ComplianceStatus.COMPLETE
    )
    onboarding: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    description: Mapped[Optional[str]] = mapped_column(String)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=utc_now, nullable=False
    )

    updated_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        onupdate=utc_now,
        nullable=False,
    )
