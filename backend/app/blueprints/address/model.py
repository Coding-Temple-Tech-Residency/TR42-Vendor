from datetime import datetime, timezone
from app.functions import generate_uuid
from app.functions import utc_now
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions import db


class Address(db.Model):
    __tablename__ = "address"

    address_id: Mapped[str] = mapped_column(
        String(36), primary_key=True, nullable=False, default=generate_uuid
    )
    street: Mapped[str] = mapped_column(String(255), nullable=False)
    city: Mapped[str] = mapped_column(String(255), nullable=False)
    state: Mapped[str] = mapped_column(String(255), nullable=False)
    zipcode: Mapped[str] = mapped_column(String(255), nullable=False)
    country: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=utc_now)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=utc_now,
        onupdate=utc_now,
    )
    created_by: Mapped[str] = mapped_column(String, nullable=False)
    updated_by: Mapped[str] = mapped_column(String)

    # relationships
    vendor: Mapped["Vendor"] = relationship(back_populates="address")
