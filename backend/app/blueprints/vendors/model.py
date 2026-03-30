from datetime import datetime, timezone
from typing import Optional
import uuid
import enum

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, DateTime, Boolean, Enum
from sqlalchemy.orm import Mapped, mapped_column
from app.extensions import db


def utc_now():
    return datetime.now(timezone.utc)


class ComplianceStatus(enum.Enum):
    EXPIRED = "expired"
    INCOMPLETE = "incomplete"
    COMPLETE = "complete"


class Vendor(db.Model):
    __tablename__ = "vendor"

    vendor_id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    company_name: Mapped[str] = mapped_column(String(80), nullable=False, unique=True)

    company_code: Mapped[Optional[str]] = mapped_column(String)

    company_email: Mapped[str] = mapped_column(String, nullable=False)
    company_phone: Mapped[str] = mapped_column(String, nullable=False)

    primary_contact_name: Mapped[Optional[str]] = mapped_column(String)

    address: Mapped[Optional[str]] = mapped_column(String)
    city: Mapped[Optional[str]] = mapped_column(String)
    state: Mapped[Optional[str]] = mapped_column(String)
    zip_code: Mapped[Optional[str]] = mapped_column(String)

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
