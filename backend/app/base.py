# This removes duplicate fields across every table
from app.extensions import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, ForeignKey
from datetime import datetime
from app.functions import utc_now


class BaseModel(db.Model):
    __abstract__ = True

    # ----------------------
    # Audit Fields
    # ----------------------
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=utc_now,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=utc_now,
        onupdate=utc_now,
    )

    created_by_user_id: Mapped[str] = mapped_column(
        ForeignKey("user.user_id"),
        nullable=False,
    )

    updated_by_user_id: Mapped[str | None] = mapped_column(
        ForeignKey("user.user_id"),
        nullable=True,
    )
