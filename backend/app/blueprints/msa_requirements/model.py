from __future__ import annotations
from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, JSON, Float, Integer, ForeignKey
from app.base import BaseModel
from app.functions import generate_uuid

if TYPE_CHECKING:
    from app.blueprints.msa.model import MSA


class MSARequirements(BaseModel):
    __tablename__ = "msa_requirements"

    id: Mapped[str] = mapped_column(
        String, primary_key=True, default=generate_uuid
    )

    msa_id: Mapped[str] = mapped_column(
        ForeignKey("msa.msa_id"), nullable=False
    )

    category: Mapped[str | None] = mapped_column(String(50))
    rule_type: Mapped[str | None] = mapped_column(String(50))
    description: Mapped[str | None] = mapped_column(Text)
    value: Mapped[str | None] = mapped_column(String(100))
    unit: Mapped[str | None] = mapped_column(String(100))
    source_field_id: Mapped[str | None] = mapped_column(String)
    page_number: Mapped[int | None] = mapped_column(Integer)
    extracted_text: Mapped[str | None] = mapped_column(Text)
    confidence_score: Mapped[float | None] = mapped_column(Float)
    requirement_metadata: Mapped[dict | None] = mapped_column(JSON)

   
    msa: Mapped["MSA"] = relationship(
        "MSA",
        back_populates="requirements"
    )

