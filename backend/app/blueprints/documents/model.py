from datetime import datetime
from sqlalchemy import ForeignKey, LargeBinary, String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.base import BaseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.blueprints.vendor.model import Vendor

class BackgroundCheck(BaseModel):
    __tablename__ = 'background_check'

    background_check_id : Mapped[str] = mapped_column(String, primary_key=True)

    background_check_passed : Mapped[bool] = mapped_column(Boolean)
    
    background_check_date : Mapped[datetime] = mapped_column(DateTime)
    
    background_check_provider : Mapped[str] = mapped_column(String)
    


class DrugTest(BaseModel):
    __tablename__ = 'drug_test'

    drug_test_id : Mapped[str] = mapped_column(String, primary_key=True)

    drug_test_passed : Mapped[bool] = mapped_column(Boolean)

    drug_test_date : Mapped[datetime] = mapped_column(DateTime)


class ComplianceDocument(BaseModel):
    __tablename__ = 'compliance_document'

    compliance_id : Mapped[str] = mapped_column(String, primary_key=True)

    vendor_id : Mapped[str] = mapped_column(String, ForeignKey('vendor.vendor_id'))

    compliance_document : Mapped[bytes] = mapped_column(LargeBinary)
    compliance_status : Mapped[bool] = mapped_column(Boolean, default=False)
    expiration_date : Mapped[datetime] = mapped_column(DateTime)

    vendor : Mapped['Vendor'] = relationship('Vendor', backref='compliance_documents')