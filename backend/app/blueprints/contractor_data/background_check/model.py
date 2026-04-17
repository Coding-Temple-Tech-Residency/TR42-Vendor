from datetime import date, datetime

from sqlalchemy import Boolean, Date, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.base import BaseModel
from app.functions import generate_uuid
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.blueprints.contractor.model import Contractor


class BackgroundCheck(BaseModel):
    __tablename__ = "background_check"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=generate_uuid,
    )

    contractor_id: Mapped[str] = mapped_column(
        ForeignKey("contractor.id"),
        nullable=False,
    )

    background_check_passed: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    background_check_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    background_check_provider: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    contractor: Mapped["Contractor"] = relationship(
        "Contractor",
        back_populates="background_checks",
    )
