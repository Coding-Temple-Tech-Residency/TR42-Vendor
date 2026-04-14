from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.base import BaseModel
from app.functions import generate_uuid
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.blueprints.contractor.model import Contractor


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
