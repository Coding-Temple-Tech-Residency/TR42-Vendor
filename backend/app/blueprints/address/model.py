from datetime import datetime
from app.functions import generate_uuid, utc_now
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.base import BaseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.blueprints.vendor.model import Vendor

class Address(BaseModel):
    __tablename__ = "address"

    address_id: Mapped[str] = mapped_column(
        String(36), primary_key=True, nullable=False, default=generate_uuid
    )
    street: Mapped[str] = mapped_column(String(255), nullable=False)
    city: Mapped[str] = mapped_column(String(255), nullable=False)
    state: Mapped[str] = mapped_column(String(255), nullable=False)
    zipcode: Mapped[str] = mapped_column(String(255), nullable=False)
    country: Mapped[str] = mapped_column(String(255), nullable=False, default="USA")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=utc_now)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=utc_now,
        onupdate=utc_now,
    )
    created_by_user_id: Mapped[str | None ] = mapped_column( # This is causing error in the deletion of a user, if it could be made to on delete set null)
        String, nullable=False
    )
    updated_by_user_id: Mapped[str | None ] = mapped_column( # Also causing error is the deletion of a user, same thing as above)
        String)
    
    # relationships
    vendor: Mapped["Vendor"] = relationship(back_populates="address")
