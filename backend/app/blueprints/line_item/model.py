from app.base import BaseModel
from sqlalchemy import ForeignKey, Numeric, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.blueprints.invoice.model import Invoice

class LineItem(BaseModel):
    __tablename__ = 'line_item'

    line_item_id : Mapped[str] = mapped_column(String, primary_key=True)
    invoice_id : Mapped[str] = mapped_column(String, ForeignKey('invoice.invoice_id'))

    quantity : Mapped[int] = mapped_column(Integer)
    rate : Mapped[float] = mapped_column(Numeric)
    amount : Mapped[float] = mapped_column(Numeric)

    invoice : Mapped ['Invoice'] = relationship('Invoice', backref='line_items')

