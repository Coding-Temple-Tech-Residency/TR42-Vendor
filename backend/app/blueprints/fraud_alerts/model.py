from __future__ import annotations
from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, DateTime, ForeignKey
from app.base import BaseModel
from app.functions import generate_uuid
import datetime

if TYPE_CHECKING:
    from app.blueprints.work_orders.model import WorkOrder
   
    # from app.blueprints.ticket.model import Ticket  # if exists


class FraudAlert(BaseModel):
    __tablename__ = "fraud_alerts"

    id: Mapped[str] = mapped_column(
        String, primary_key=True, default=generate_uuid
    )

    work_order_id: Mapped[str | None] = mapped_column(
        ForeignKey("work_orders.work_order_id"), nullable=True
    )

    # ticket_id: Mapped[str | None] = mapped_column(
    #     ForeignKey("ticket.ticket_id")
    # )
    ticket_id: Mapped[str | None] = mapped_column(String, nullable=True)
    severity: Mapped[str | None] = mapped_column(String(100))
    description: Mapped[str | None] = mapped_column(Text)
    status: Mapped[str | None] = mapped_column(String)
    flagged_at: Mapped[datetime.datetime | None] = mapped_column(DateTime)
    
    work_order: Mapped["WorkOrder"] = relationship(
        "WorkOrder",
        back_populates="fraud_alerts"
    )
    # ticket: Mapped["Ticket"] = relationship(
    #     "Ticket",
    #     back_populates="fraud_alerts"
    # )