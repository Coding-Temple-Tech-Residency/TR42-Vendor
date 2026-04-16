from datetime import date, datetime

from sqlalchemy import Boolean, Date, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.base import BaseModel
from app.functions import generate_uuid
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.blueprints.contractor.model import Contractor
    from app.blueprints.user.model import User


class License(BaseModel):
    __tablename__ = "license"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=generate_uuid,
    )

    contractor_id: Mapped[str] = mapped_column(
        ForeignKey("contractor.id"),
        nullable=False,
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

    license_document_url: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    license_verified: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    license_verified_by: Mapped[str | None] = mapped_column(
        ForeignKey("user.id"),
        nullable=True,
    )

    license_verified_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    contractor: Mapped["Contractor"] = relationship(
        "Contractor",
        back_populates="licenses",
    )

    verified_by_user: Mapped["User | None"] = relationship(
        "User",
        foreign_keys=[license_verified_by],
    )
