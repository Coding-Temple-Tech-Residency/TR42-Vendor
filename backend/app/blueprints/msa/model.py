from __future__ import annotations
from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Date, DateTime
import datetime
from app.functions import generate_uuid
from app.base import BaseModel

if TYPE_CHECKING:
    from app.blueprints.vendor.model import Vendor
    from app.blueprints.user.model import User
    from app.blueprints.msa_requirements.model import MSARequirements
   


class MSA(BaseModel):
    __tablename__ = "msa"

    # PRIMARY KEY
    id: Mapped[str] = mapped_column(
        String, primary_key=True, default=generate_uuid
    )

    # FOREIGN KEY (NOT NULL)
    vendor_id: Mapped[str] = mapped_column(
        ForeignKey("vendor.vendor_id"),
        nullable=False
    )

    # OPTIONAL FIELDS
    version: Mapped[str | None] = mapped_column(String(10))
    effective_date: Mapped[datetime.date | None] = mapped_column(Date)
    expiration_date: Mapped[datetime.date | None] = mapped_column(Date)
    status: Mapped[str | None] = mapped_column(String(15))

    # FOREIGN KEY (NULLABLE)
    uploaded_by: Mapped[str | None] = mapped_column(
        ForeignKey("user.user_id"),
        nullable=False
    )


    # RELATIONSHIPS
    vendor: Mapped["Vendor"] = relationship(back_populates="msas")

    uploaded_by_user: Mapped["User"] = relationship(
        "User",
        foreign_keys=[uploaded_by],
        back_populates="msas_uploaded",
    )

    requirements: Mapped[list["MSARequirements"]] = relationship(
        "MSARequirements",
        back_populates="msa",
        cascade="all, delete-orphan"
    )
