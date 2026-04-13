from app.base import BaseModel
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from app.base import BaseModel
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.blueprints.work_orders.model import WorkOrder
    from app.blueprints.ticket.model import Ticket
    from app.blueprints.vendor.model import Vendor

class Invoice(BaseModel):
    __tablename__ = 'invoice'

    invoice_id : Mapped [str] = mapped_column(String, primary_key=True)

    work_order_id : Mapped [str] = mapped_column(
        String,
        ForeignKey('work_orders.work_order_id')
    )
    ticket_id : Mapped [str] = mapped_column(
        String,
        ForeignKey('ticket.ticket_id')
    )
    vendor_id : Mapped [str] = mapped_column(
        String,
        ForeignKey('vendor.vendor_id')
    )

    total_amount : Mapped [str] = mapped_column(String)

    invoice_status : Mapped [str] = mapped_column(
        String,
        nullable=False
    )