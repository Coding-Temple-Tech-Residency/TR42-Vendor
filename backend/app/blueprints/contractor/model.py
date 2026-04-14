from app.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Enum, String, ForeignKey, Integer, Float
from app.functions import generate_uuid
import enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.blueprints.user.model import User
    from app.blueprints.vendor_contractor.model import VendorContractor
    from app.blueprints.contractor_data.background_check.model import BackgroundCheck
    from app.blueprints.contractor_data.drug_test.model import DrugTest
    from app.blueprints.contractor_data.license.model import License
    from app.blueprints.contractor_data.biometric_data.model import BiometricData
    from app.blueprints.contractor_data.insurance.model import Insurance
    from app.blueprints.contractor_data.certification.model import Certification


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

    vendor_manager_id: Mapped[str | None] = mapped_column(
        ForeignKey("user.user_id"),
        nullable=True,
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
    is_onboarded: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    is_subcontractor: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False
    )
    is_fte: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    is_licensed: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    is_insured: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    is_certified: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    average_rating: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    years_experience: Mapped[int | None] = mapped_column(Integer, nullable=True)

    user: Mapped["User"] = relationship(
        "User",
        back_populates="contractor_profile",
        foreign_keys=[user_id],
    )

    vendor_manager: Mapped["User | None"] = relationship(
        "User",
        foreign_keys=[vendor_manager_id],
    )

    vendor_links: Mapped[list["VendorContractor"]] = relationship(
        "VendorContractor",
        back_populates="contractor",
        foreign_keys="VendorContractor.contractor_id",
        cascade="all, delete-orphan",
    )

    background_check: Mapped["BackgroundCheck | None"] = relationship(
        "BackgroundCheck",
        back_populates="contractor",
        uselist=False,
        cascade="all, delete-orphan",
        single_parent=True,
    )

    drug_test: Mapped["DrugTest | None"] = relationship(
        "DrugTest",
        back_populates="contractor",
        uselist=False,
        cascade="all, delete-orphan",
        single_parent=True,
    )

    license: Mapped["License | None"] = relationship(
        "License",
        back_populates="contractor",
        uselist=False,
        cascade="all, delete-orphan",
        single_parent=True,
    )

    biometrics: Mapped[list["BiometricData"]] = relationship(
        "BiometricData",
        back_populates="contractor",
        cascade="all, delete-orphan",
    )

    insurances: Mapped[list["Insurance"]] = relationship(
        "Insurance",
        back_populates="contractor",
        cascade="all, delete-orphan",
    )

    certifications: Mapped[list["Certification"]] = relationship(
        "Certification",
        back_populates="contractor",
        cascade="all, delete-orphan",
    )
