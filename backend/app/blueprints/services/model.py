
from app.functions import generate_uuid
from typing import TYPE_CHECKING
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.base import BaseModel
from app.extensions import db
from app.blueprints.vendor_service.model import VendorService

if TYPE_CHECKING:
    #from app.blueprints.vendor_services.model import VendorService
    from app.blueprints.user.model import User

class Service(BaseModel):
    __tablename__ = "services"

    service_id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        nullable=False,
        default=generate_uuid
    )

    service: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True
    )

    created_by: Mapped[str] = mapped_column(
        ForeignKey("user.user_id"),
        nullable=False,
    )

    updated_by: Mapped[str] = mapped_column(
        ForeignKey("user.user_id"),
        nullable=False,
    )

    vendor_id = db.Column(
        db.String,
        db.ForeignKey('vendor.id')
    )

    vendor_links: Mapped[list["VendorService"]] = relationship(
        "VendorService",
        back_populates="service",
        cascade="all, delete-orphan"
    )
  
    service_id = db.Column(
        db.String,
        db.ForeignKey('services.id')
    )

    # relationships
    vendor = db.relationship('Vendor', backref='services_link')
    service = db.relationship('Service', back_populates='vendors')
