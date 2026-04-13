from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.base import BaseModel

class ContractorPerformance(BaseModel): 
    __tablename__ = 'contractor_performance'

    rating_id : Mapped [String]= mapped_column(String, primary_key=True)
    
    rating : Mapped [Integer] = mapped_column(Integer) #1.0 to 5.0
    
    comments : Mapped [String] = mapped_column(String)
    
    ticket_id : Mapped [String] = mapped_column(String, ForeignKey('ticket.ticket_id'))
    
    contractor_id : Mapped [String] = mapped_column(String, ForeignKey('contractors.contractor_id'))
