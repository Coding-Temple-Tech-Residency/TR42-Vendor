from datetime import date
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Date, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.base import BaseModel
from app.functions import generate_uuid

if TYPE_CHECKING:
    from app.blueprints.contractor.model import Contractor


class Insurance(BaseModel):
    __tablename__ = "insurance"

    insurance_id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=generate_uuid,
    )

    contractor_id: Mapped[str] = mapped_column(
        ForeignKey("contractor.id"),
        nullable=False,
    )

    insurance_type: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    policy_number: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    provider_name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    provider_phone: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    coverage_amount: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
        nullable=True,
    )

    deductible: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
        nullable=True,
    )

    effective_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    expiration_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    insurance_document_url: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    insurance_verified: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    additional_insurance_required: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    additional_insured_certificate_url: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    contractor: Mapped["Contractor"] = relationship(
        "Contractor",
        back_populates="insurances",
    )
