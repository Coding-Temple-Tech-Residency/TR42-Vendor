from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, UniqueConstraint
from app.functions import generate_uuid
from app.base import BaseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.blueprints.user.model import User


class VendorService(BaseModel):
    __tablename__ = "vendor_service"
    __table_args__ = (
        UniqueConstraint("vendor_id", "service_id", name="uq_vendor_service_pair"),
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)

    vendor_id: Mapped[str] = mapped_column(ForeignKey("vendor.id"), nullable=False)

    service_id: Mapped[str] = mapped_column(ForeignKey("service.id"), nullable=False)

    vendor = relationship("Vendor", back_populates="service_links")
    service = relationship("Service", back_populates="vendor_links")
