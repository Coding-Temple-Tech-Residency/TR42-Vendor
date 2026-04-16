from datetime import datetime
import enum

from sqlalchemy import DateTime, Enum, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.blueprints.user.model import User
from app.blueprints.vendor.model import Vendor

from app.extensions import db
from app.functions import generate_uuid, utc_now


class VendorUserRole(enum.Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    USER = "user"


class VendorUser(db.Model):
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
        ForeignKey("user.id"),
        nullable=False,
    )

    vendor_id: Mapped[str] = mapped_column(
        ForeignKey("vendor.id"),
        nullable=False,
    )

    vendor_user_role: Mapped[VendorUserRole] = mapped_column(
        Enum(VendorUserRole, name="vendor_user_role"),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(DateTime, default=utc_now)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=utc_now,
        onupdate=utc_now,
    )

    created_by_user_id: Mapped[str] = mapped_column(
        ForeignKey("user.user_id"),
        nullable=False,
    )

    updated_by_user_id: Mapped[str | None] = mapped_column(
        ForeignKey("user.user_id"),
        nullable=True,
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="vendor_links",
        foreign_keys=[user_id],
    )

    created_by_user: Mapped["User"] = relationship(
        "User",
        foreign_keys=[created_by_user_id],
    )

    updated_by_user: Mapped["User | None"] = relationship(
        "User",
        foreign_keys=[updated_by_user_id],
    )

    vendor: Mapped["Vendor"] = relationship(
        "Vendor",
        back_populates="vendor_links",
    )