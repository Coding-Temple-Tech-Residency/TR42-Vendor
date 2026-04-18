from app.extensions import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from app.functions import generate_uuid
from app.base import BaseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
   
    from app.blueprints.user.model import User


class VendorService(db.Model):
    __tablename__ = "vendor_service"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=generate_uuid
    )

    vendor_id: Mapped[str] = mapped_column(
        ForeignKey("vendor.vendor_id"),
        nullable=False
    )

    service_id: Mapped[str] = mapped_column(
        ForeignKey("services.service_id"),
        nullable=False
    )

    created_by: Mapped[str] = mapped_column(
        ForeignKey("user.user_id"),
        nullable=False,
    )

    updated_by: Mapped[str] = mapped_column(
        ForeignKey("user.user_id"),
        nullable=False,
    )

    # Relationships
    created_by_user: Mapped["User"] = relationship(
        "User",
        foreign_keys=[created_by]
    )

    updated_by_user: Mapped["User"] = relationship(
        "User",
        foreign_keys=[updated_by]
    )

    vendor = relationship("Vendor", back_populates="service_links")
    service = relationship("Service", back_populates="vendor_links")
