from app.extensions import db
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import Numeric
from app.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Enum, String, ForeignKey, Integer, Float
from app.functions import generate_uuid
import enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.blueprints.user.model import User
    from app.blueprints.vendor_contractor.model import VendorContractor
    from app.blueprints.compliance_document.model import BackgroundCheck
    from app.blueprints.compliance_document.model import DrugTest
    from app.blueprints.compliance_document.model import License


class ContractorStatus(enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class Contractor(BaseModel):
    __tablename__ = "contractor"

    contractor_id: Mapped[str] = mapped_column(
        String(36), primary_key=True, nullable=False, default=generate_uuid
    )

    user_id: Mapped[str] = mapped_column(
        ForeignKey("user.user_id"),
        nullable=False,
        unique=True,
    )

    employee_number: Mapped[str] = mapped_column(String, nullable=False)

    vendor_manager_id: Mapped[str] = mapped_column(
        ForeignKey("user.user_id"),
        unique=False,
    )

    status: Mapped[ContractorStatus] = mapped_column(
        Enum(ContractorStatus, name="contractor_status"),
        nullable=False,
        default=ContractorStatus.ACTIVE,
    )

    tickets_completed: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    tickets_open: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    biometric_enrolled: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False
    )
    is_onboarded: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    is_subcontractor: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False
    )
    is_fte: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    is_licensed: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    is_insured: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    is_certified: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    average_rating: Mapped[float] = mapped_column(Float, nullable=False, default=0.00)
    years_experience: Mapped[int] = mapped_column(Integer, nullable=True)

    background_check_id: Mapped[str] = mapped_column(
        String, nullable=True, default=generate_uuid
    )
    drug_test_id: Mapped[str] = mapped_column(
        String, nullable=True, default=generate_uuid
    )
    # preferred_job_types

    # Relationships
    user: Mapped["User"] = relationship(
        "User",
        back_populates="contractor_profile",
        foreign_keys=[user_id],
    )

    vendor_manager: Mapped["User"] = relationship(
        "User",
        foreign_keys=[vendor_manager_id],
    )

    vendor_links: Mapped[list["VendorContractor"]] = relationship(
        "VendorContractor",
        back_populates="contractor",
        foreign_keys="VendorContractor.contractor_id",
        cascade="all, delete-orphan",
    )

    background_check: Mapped["BackgroundCheck"] = relationship(
        "BackgroundCheck",
        back_populates="contractor",
        uselist=False,
        cascade="all, delete-orphan",
    )

    drug_test: Mapped["DrugTest"] = relationship(
        "DrugTest",
        back_populates="contractor",
        uselist=False,
        cascade="all, delete-orphan",
    )

    license: Mapped["License"] = relationship(
        "License",
        back_populates="contractor",
        uselist=False,
        cascade="all, delete-orphan",
    )
