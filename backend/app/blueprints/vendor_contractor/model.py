import enum

from sqlalchemy import Enum, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.extensions import db
from app.base import BaseModel
from app.functions import generate_uuid
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.blueprints.contractor.model import Contractor
    from app.blueprints.vendor.model import Vendor
    from app.blueprints.user.model import User


class VendorContractorRole(enum.Enum):
    DRIVER = "driver"
    WORKER = "worker"
    PRIVATE_CONTRACTOR = "private_contractor"


class VendorContractor(BaseModel):
    __tablename__ = "vendor_contractor"
    __table_args__ = (
        UniqueConstraint(
            "contractor_id", "vendor_id", name="uq_vendor_contractor_contractor_vendor"
        ),
    )

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        nullable=False,
        default=generate_uuid,
    )

    manager_id: Mapped[str] = mapped_column(
        ForeignKey("user.id"),
        nullable=False,
    )

    contractor_id: Mapped[str] = mapped_column(
        ForeignKey("contractor.id"),
        nullable=False,
    )

    vendor_id: Mapped[str] = mapped_column(
        ForeignKey("vendor.id"),
        nullable=False,
    )

    vendor_contractor_role: Mapped[VendorContractorRole] = mapped_column(
        Enum(VendorContractorRole, name="vendor_contractor_role"),
        nullable=False,
    )

    # Relationships

    manager: Mapped["User"] = relationship(
        "User",
        foreign_keys=[manager_id],
        back_populates="managed_contractor_links",
    )

    contractor: Mapped["Contractor"] = relationship(
        "Contractor",
        back_populates="vendor_links",
        foreign_keys=[contractor_id],
    )

    vendor: Mapped["Vendor"] = relationship(
        "Vendor",
        back_populates="contractor_links",
        foreign_keys=[vendor_id],
    )
