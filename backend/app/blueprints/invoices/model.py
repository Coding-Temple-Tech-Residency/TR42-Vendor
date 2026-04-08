from sqlalchemy import String, Integer, Numeric, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.base import BaseModel

class Invoice(BaseModel):
    __tablename__ = 'invoice'

    invoice_id: Mapped[str] = mapped_column(String, primary_key=True)
    work_order_id: Mapped[str] = mapped_column(String, ForeignKey('work_orders.work_order_id'), nullable=False)
    ticket_id: Mapped[str] = mapped_column(String, ForeignKey('ticket.ticket_id'), nullable=False)
    vendor_id: Mapped[str] = mapped_column(String, ForeignKey('vendor.vendor_id'), nullable=False)
    invoice_date: Mapped[str] = mapped_column(String, nullable=False)
    total_amount: Mapped[Numeric] = mapped_column(Numeric)
    invoice_status: Mapped[str] = mapped_column(Enum('accepted', 'pending', 'rejected', name='invoice_status'))
    due_date: Mapped[str] = mapped_column(String, nullable=False)
    period_start: Mapped[str] = mapped_column(String)
    period_end: Mapped[str] = mapped_column(String)

    line_items: Mapped[list['LineItem']] = relationship('LineItem', back_populates='invoice', cascade='all, delete-orphan')


class LineItem(BaseModel):
    __tablename__ = 'line_item'

    line_item_id: Mapped[str] = mapped_column(String, primary_key=True)
    invoice_id: Mapped[str] = mapped_column(String, ForeignKey('invoice.invoice_id'), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer)
    rate: Mapped[Numeric] = mapped_column(Numeric)
    amount: Mapped[Numeric] = mapped_column(Numeric)
    description: Mapped[str] = mapped_column(String)

    invoice: Mapped['Invoice'] = relationship('Invoice', back_populates='line_items')