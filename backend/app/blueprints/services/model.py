from app.functions import generate_uuid
from typing import TYPE_CHECKING
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.base import BaseModel

if TYPE_CHECKING:
    from app.blueprints.vendor_service.model import VendorService


class Service(BaseModel):
    __tablename__ = "service"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, nullable=False, default=generate_uuid
    )

    service: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)

    vendor_links: Mapped[list["VendorService"]] = relationship(
        "VendorService", back_populates="service", cascade="all, delete-orphan"
    )
