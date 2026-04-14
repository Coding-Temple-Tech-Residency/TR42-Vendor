from sqlalchemy import ForeignKey, LargeBinary, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from app.base import BaseModel
from app.functions import generate_uuid

if TYPE_CHECKING:
    from app.blueprints.contractor.model import Contractor


class BiometricData(BaseModel):
    __tablename__ = "biometric_data"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=generate_uuid,
    )

    contractor_id: Mapped[str] = mapped_column(
        ForeignKey("contractor.contractor_id"),
        nullable=False,
    )

    biometric_enrollment_data: Mapped[bytes | None] = mapped_column(
        LargeBinary,
        nullable=True,
    )

    contractor: Mapped["Contractor"] = relationship(
        "Contractor",
        back_populates="biometrics",
    )
