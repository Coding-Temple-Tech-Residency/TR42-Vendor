from datetime import datetime
import enum
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Enum, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.extensions import db
from app.functions import generate_uuid, utc_now
from app.base import BaseModel

if TYPE_CHECKING:
    from app.blueprints.user.model import User
    from app.blueprints.vendor.model import Vendor

class VendorUserRole(enum.Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    USER = "user"


class VendorUser(BaseModel):
    __tablename__ = "vendor_user"
    __table_args__ = (
        UniqueConstraint("user_id", "vendor_id", name="uq_vendor_user_user_vendor"),
    )

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=generate_uuid,
    )

    user_id: Mapped[str] = mapped_column(
        ForeignKey("user.user_id"),
        nullable=False,
    )

    vendor_id: Mapped[str] = mapped_column(
        ForeignKey("vendor.vendor_id"),
        nullable=False,
    )

    vendor_user_role: Mapped[VendorUserRole] = mapped_column(
        Enum(VendorUserRole, name="vendor_user_role"),
        nullable=False,
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="vendor_links",
        foreign_keys=[user_id],
    )

    vendor: Mapped["Vendor"] = relationship(
        "Vendor",
        back_populates="vendor_links",
    )