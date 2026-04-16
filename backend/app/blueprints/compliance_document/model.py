from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, DateTime, ForeignKey, LargeBinary, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.base import BaseModel
from app.functions import generate_uuid

if TYPE_CHECKING:
    from app.blueprints.vendor.model import Vendor


class ComplianceDocument(BaseModel):
    __tablename__ = "compliance_document"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=generate_uuid,
    )

    vendor_id: Mapped[str] = mapped_column(
        ForeignKey("vendor.id"),
        nullable=False,
    )

    compliance_document: Mapped[bytes] = mapped_column(
        LargeBinary,
        nullable=True,
    )

    compliance_status: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    expiration_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=True,
    )

    vendor: Mapped["Vendor"] = relationship(
        "Vendor",
        back_populates="compliance_documents",
    )
