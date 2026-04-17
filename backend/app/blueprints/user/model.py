from datetime import date, datetime
import enum
from app.functions import generate_uuid, utc_now
from typing import TYPE_CHECKING
from sqlalchemy import (
    Boolean,
    Date,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    LargeBinary,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.auth.passwords import hash_password, verify_password

from app.extensions import db

if TYPE_CHECKING:
    from app.blueprints.vendor_user.model import VendorUser
    from app.blueprints.contractor.model import Contractor
    from app.blueprints.address.model import Address
    from app.blueprints.vendor_contractor.model import VendorContractor


class UserType(enum.Enum):
    OPERATOR = "operator"
    VENDOR = "vendor"
    CONTRACTOR = "contractor"


class User(db.Model):
    __tablename__ = "user"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=generate_uuid,
    )

    username: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)

    user_type: Mapped[UserType] = mapped_column(
        Enum(UserType, name="user_type"), nullable=False, index=True
    )
    token_version: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    is_active: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=True, index=True
    )
    is_admin: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    profile_photo: Mapped[bytes | None] = mapped_column(LargeBinary, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=utc_now, index=True
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=utc_now, nullable=False, onupdate=utc_now, index=True
    )

    created_by: Mapped[str | None] = mapped_column(ForeignKey("user.id"), nullable=True)
    updated_by: Mapped[str | None] = mapped_column(ForeignKey("user.id"), nullable=True)

    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    middle_name: Mapped[str] = mapped_column(String(50), nullable=True)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)

    contact_number: Mapped[str] = mapped_column(String, nullable=False)
    alternate_number: Mapped[str] = mapped_column(String, nullable=True)

    date_of_birth: Mapped[date | None] = mapped_column(Date, nullable=True)

    ssn_last_four: Mapped[str | None] = mapped_column(String(4), nullable=True)

    address_id: Mapped[str] = mapped_column(
        ForeignKey("address.id"), nullable=True, unique=True
    )

    # Relationships

    address: Mapped["Address"] = relationship(
        "Address",
        back_populates="user",
        foreign_keys=[address_id],
    )

    created_by_user: Mapped["User | None"] = relationship(
        "User",
        foreign_keys=[created_by],
        remote_side=[id],
    )

    updated_by_user: Mapped["User | None"] = relationship(
        "User",
        foreign_keys=[updated_by],
        remote_side=[id],
    )

    vendor_links: Mapped[list["VendorUser"]] = relationship(
        "VendorUser",
        back_populates="user",
        foreign_keys="VendorUser.user_id",
        cascade="all, delete-orphan",
    )

    managed_contractor_links: Mapped[list["VendorContractor"]] = relationship(
        "VendorContractor",
        foreign_keys="VendorContractor.manager_id",
        back_populates="manager",
    )

    contractor_profile: Mapped["Contractor | None"] = relationship(
        "Contractor",
        back_populates="user",
        uselist=False,
        foreign_keys="Contractor.user_id",
        cascade="all, delete-orphan",
    )

    def set_password(self, raw_password: str) -> None:
        self.password_hash = hash_password(raw_password)

    def check_password(self, raw_password: str) -> bool:
        return verify_password(raw_password, self.password_hash)
