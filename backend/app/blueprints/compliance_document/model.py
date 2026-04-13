from datetime import date, datetime
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Date, DateTime, ForeignKey, LargeBinary, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.base import BaseModel
from app.functions import generate_uuid, utc_now

if TYPE_CHECKING:
    from app.blueprints.contractor.model import Contractor
    from app.blueprints.vendor.model import Vendor
    from app.blueprints.user.model import User


class BackgroundCheck(BaseModel):
    __tablename__ = "background_check"

    background_check_id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=generate_uuid,
    )

    contractor_id: Mapped[str] = mapped_column(
        ForeignKey("contractor.contractor_id"),
        nullable=False,
        unique=True,
    )

    background_check_passed: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    background_check_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=True,
    )

    background_check_provider: Mapped[str] = mapped_column(
        String,
        nullable=True,
    )

    contractor: Mapped["Contractor"] = relationship(
        "Contractor",
        back_populates="background_check",
    )


class DrugTest(BaseModel):
    __tablename__ = "drug_test"

    drug_test_id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=generate_uuid,
    )

    contractor_id: Mapped[str] = mapped_column(
        ForeignKey("contractor.contractor_id"),
        nullable=False,
        unique=True,
    )

    drug_test_passed: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    drug_test_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=True,
    )

    contractor: Mapped["Contractor"] = relationship(
        "Contractor",
        back_populates="drug_test",
    )


class ComplianceDocument(BaseModel):
    __tablename__ = "compliance_document"

    compliance_id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=generate_uuid,
    )

    vendor_id: Mapped[str] = mapped_column(
        ForeignKey("vendor.vendor_id"),
        nullable=False,
    )

    compliance_document: Mapped[bytes] = mapped_column(
        LargeBinary,
        nullable=True,
    )

    compliance_status: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    expiration_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=True,
    )

    vendor: Mapped["Vendor"] = relationship(
        "Vendor",
        back_populates="compliance_documents",
    )


class License(BaseModel):
    __tablename__ = "license"

    license_id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=generate_uuid,
    )

    contractor_id: Mapped[str] = mapped_column(
        ForeignKey("contractor.contractor_id"),
        nullable=False,
        unique=True,
    )

    license_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    license_number: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    license_state: Mapped[str] = mapped_column(
        String(2),
        nullable=False,
    )

    license_expiration_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    license_document_url: Mapped[str] = mapped_column(
        String(255),
        nullable=True,
    )

    license_verified: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    license_verified_by: Mapped[str] = mapped_column(
        ForeignKey("user.user_id"),
        nullable=True,
    )

    license_verified_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=True,
    )

    contractor: Mapped["Contractor"] = relationship(
        "Contractor",
        back_populates="license",
    )

    verified_by_user: Mapped["User"] = relationship(
        "User",
        foreign_keys=[license_verified_by],
    )
