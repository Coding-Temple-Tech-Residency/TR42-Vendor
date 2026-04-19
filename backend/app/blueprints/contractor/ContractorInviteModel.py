from app.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey, DateTime, Boolean
from datetime import datetime, timedelta
from app.functions import generate_uuid, utc_now


class ContractorInvite(BaseModel):
    __tablename__ = "contractor_invite"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=generate_uuid
    )

    token: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    vendor_id: Mapped[str] = mapped_column(
        ForeignKey("vendor.id"), nullable=False
    )

    vendor_manager_id: Mapped[str | None] = mapped_column(
        ForeignKey("user.id"), nullable=True
    )

    email: Mapped[str] = mapped_column(String, nullable=False)

    is_used: Mapped[bool] = mapped_column(Boolean, default=False)

    expires_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False
    )