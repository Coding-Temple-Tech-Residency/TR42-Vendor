from sqlalchemy import Boolean, ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.base import BaseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.blueprints.contractors.model import Contractor

class Insurance(BaseModel):

    __tablename__ = 'insurance'

    insurance_id : Mapped [str] = mapped_column(String, primary_key=True) 
    
    contractor_id : Mapped [str] = mapped_column(
        String,
        ForeignKey('contractors.contractor_id'),
        nullable=False
    )
    insurance_type : Mapped [str] = mapped_column(String, nullable=False)
    
    policy_number : Mapped [int] = mapped_column(Integer, nullable=False)
    
    provider_name : Mapped [str] = mapped_column(String, nullable=False)
    
    provider_phone : Mapped [str] = mapped_column(String, nullable=False)
    
    coverage_amount : Mapped [str] = mapped_column(String)
    
    deductible : Mapped [str] = mapped_column(String)
    
    effective_date : Mapped [str] = mapped_column(String)
    
    expiration_date : Mapped [str] = mapped_column(String)
    
    insurance_document_url : Mapped [str] = mapped_column(String(100))
    
    insurance_verified : Mapped [bool] = mapped_column(Boolean, default=False)
    
    additional_insurance_required : Mapped [bool] = mapped_column(Boolean)
    
    additional_insured_certificate_url : Mapped [str] = mapped_column(String(100))
