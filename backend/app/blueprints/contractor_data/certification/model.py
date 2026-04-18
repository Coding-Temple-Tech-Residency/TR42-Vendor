from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.base import BaseModel
from app.functions import generate_uuid

if TYPE_CHECKING:
    from app.blueprints.contractor.model import Contractor


class Certification(BaseModel):
    __tablename__ = "certification"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=generate_uuid,
    )

    contractor_id: Mapped[str] = mapped_column(
        ForeignKey("contractor.id"),
        nullable=False,
    )

    certification_name: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    certifying_body: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    certification_number: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    issue_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    expiration_date: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    certification_document_url: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    certification_verified: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    contractor: Mapped["Contractor"] = relationship(
        "Contractor",
        back_populates="certifications",
    )
