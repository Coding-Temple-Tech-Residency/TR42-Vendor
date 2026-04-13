from sqlalchemy import  ForeignKey, String, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models import BaseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.blueprints.work_orders.model import WorkOrder
    from app.blueprints.ticket.model import Ticket
    
class FraudAlert(BaseModel):
    __tablename__ = 'fraud_alerts'

    id : Mapped [str] = mapped_column (String, primary_key=True)

    work_order_id : Mapped [str] = mapped_column(
        String,
        ForeignKey('work_orders.work_order_id')
    )

    ticket_id : Mapped [str] = mapped_column(
        String,
        ForeignKey('ticket.ticket_id')
    )

    severity : Mapped [str] = mapped_column(String(100))
    description : Mapped [str] = mapped_column(Text)
    status : Mapped [str] = mapped_column(String)

    flagged_at : Mapped [str] = mapped_column(DateTime)

    # relationships
    work_order : Mapped ['WorkOrder'] = relationship('WorkOrder', backref='fraud_alerts')
    ticket : Mapped ['Ticket'] = relationship('Ticket', backref='fraud_alerts')