from app.extensions import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from app.functions import generate_uuid
from app.base import BaseModel

from typing import TYPE_CHECKING

if TYPE_CHECKING:
   from app.blueprints.vendor.model import Vendor
   from app.blueprints.services.model import Service
        
    


class VendorService(BaseModel,db.Model):
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

    
    vendor = relationship("Vendor", back_populates="service_links")
    service = relationship("Service", back_populates="vendor_links")
