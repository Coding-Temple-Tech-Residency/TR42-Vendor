from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.base import BaseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.blueprints.contractors.model import Contractor
    from app.blueprints.vendor.model import Vendor


class License(BaseModel):
    __tablename__ = 'licenses'

    license_id : Mapped [str] = mapped_column(String, primary_key=True)

    contractor_id : Mapped [str] = mapped_column(
        String,
        ForeignKey('contractors.contractor_id'),
        nullable=False
    )

    license_type : Mapped [str] = mapped_column(String(100), nullable=False)
    license_number : Mapped [str] = mapped_column(String(100), nullable=False)
    license_state : Mapped [str] = mapped_column(String(2), nullable=False)

    license_expiration_date : Mapped [str] = mapped_column(String, nullable=False)

    license_document_url : Mapped [str] = mapped_column(String(100))

    license_verified : Mapped [bool] = mapped_column(Boolean, default=False)

    license_verified_by : Mapped [str] = mapped_column(
        String,
        ForeignKey('vendor.vendor_id')  # verifier is a vendor
    )

    license_verified_at : Mapped [str] = mapped_column(String)


    # ----------------------
    # 🔗 Relationships
    # ----------------------

    contractor : Mapped ['Contractor'] = relationship('Contractor',foreign_keys=[contractor_id], backref='licenses')

    verifier : Mapped ['Vendor'] = relationship('Vendor', backref='verified_licenses')

