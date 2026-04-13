from sqlalchemy import Integer
from datetime import datetime
from sqlalchemy import ForeignKey, String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.base import BaseModel      
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.blueprints.contractors.model import Contractor

class Certification(BaseModel):
    __tablename__ = 'certifications'

    certification_id: Mapped[str] = mapped_column(primary_key=True)

    contractor_id: Mapped[str] = mapped_column(String, ForeignKey('contractors.contractor_id'), nullable=False)

    certification_name: Mapped[str] = mapped_column(String)
    certifying_body: Mapped[str] = mapped_column(String)

    certification_number: Mapped[int] = mapped_column(Integer, nullable=False)

    issue_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    expiration_date: Mapped[datetime] = mapped_column(DateTime)

    certification_document_url: Mapped[str] = mapped_column(String(100))

    certification_verified: Mapped[bool] = mapped_column(Boolean, default=False)


    # ----------------------
    # 🔗 Relationships
    # ----------------------

    contractor : Mapped['Contractor'] = relationship(backref='certifications')
