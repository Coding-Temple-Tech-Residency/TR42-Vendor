from datetime import datetime
from app.functions import generate_uuid, utc_now
from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions import db
from typing import TYPE_CHECKING
from app.base import BaseModel

if TYPE_CHECKING:
    from app.blueprints.vendor.model import Vendor


class Address(BaseModel):
    __tablename__ = "address"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, nullable=False, default=generate_uuid
    )
    street: Mapped[str] = mapped_column(String(255), nullable=False)
    city: Mapped[str] = mapped_column(String(255), nullable=False)
    state: Mapped[str] = mapped_column(String(255), nullable=False)
    zipcode: Mapped[str] = mapped_column(String(255), nullable=False)
    country: Mapped[str] = mapped_column(String(255), nullable=False, default="USA")

    # relationships
    vendor: Mapped["Vendor"] = relationship(back_populates="address")
