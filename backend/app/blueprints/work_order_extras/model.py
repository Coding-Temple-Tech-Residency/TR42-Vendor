from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.base import BaseModel
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.blueprints.work_orders.model import WorkOrder
    from app.blueprints.vendor.model import Vendor

class CancelledWorkOrder(BaseModel):
    __tablename__ = 'cancelled_work_orders'

    id : Mapped[str] = mapped_column(primary_key=True)

    work_order_id : Mapped[str] = mapped_column(ForeignKey('work_orders.work_order_id'),nullable=False)

    vendor_id : Mapped[str] = mapped_column(ForeignKey('vendor.vendor_id'),nullable=False)

    cancellation_reason : Mapped[str] = mapped_column(Text, nullable=False) 


    # relationships
    work_order :    Mapped ['WorkOrder'] = relationship('WorkOrder', backref='cancellations')
    vendor : Mapped ['Vendor'] = relationship('Vendor', backref='cancelled_work_orders')