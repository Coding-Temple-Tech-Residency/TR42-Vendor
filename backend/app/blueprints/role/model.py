from typing import TYPE_CHECKING
from sqlalchemy import String, Text, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.base import BaseModel
from app.functions import generate_uuid
import enum

if TYPE_CHECKING:
    from app.blueprints.vendor_user.model import VendorUser


class RoleOptions(enum.Enum):
    USER = "USER"
    MANAGER = "MANAGER"
    ADMIN = "ADMIN"


class Role(BaseModel):
    __tablename__ = "role"

    role_id: Mapped[str] = mapped_column(
        String(36), primary_key=True, nullable=False, default=generate_uuid
    )

    role_name: Mapped[str] = mapped_column(String(100), nullable=False)

    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    role_options: Mapped[RoleOptions] = mapped_column(
        Enum(RoleOptions, name="role_options"),
        nullable=False,
    )

    # relationships
    vendor_users: Mapped[list["VendorUser"]] = relationship(
        back_populates="role_ref",
        cascade="all, delete-orphan",
    )
