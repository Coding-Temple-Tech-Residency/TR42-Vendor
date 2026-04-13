from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import ForeignKey, String, Boolean, DateTime, Numeric, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.base import BaseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.blueprints.vendor.model import Vendor
    from app.blueprints.address.model import Address
    from app.blueprints.documents.model import BackgroundCheck, DrugTest


class Contractor(BaseModel):
    __tablename__ = 'contractors'

    contractor_id : Mapped[str] = mapped_column(String, primary_key=True)

    employee_number : Mapped [str] =  mapped_column(String, nullable=False)

    vendor_id : Mapped [str] = mapped_column(
        String,
        ForeignKey('vendor.vendor_id'),
        nullable=False
    )

    vendor_manager_id : Mapped [str] = mapped_column(
        String,
        ForeignKey('contractors.contractor_id'),
        nullable=True  # allow null for top-level managers
    )

    # 🧑 Personal Info
    first_name : Mapped [str] = mapped_column(String(80))
    last_name : Mapped [str] = mapped_column(String(80))
    middle_name : Mapped [str] = mapped_column(String(80))

    date_of_birth : Mapped [str] =  mapped_column(DateTime)
    ssn_last_four : Mapped [str] = mapped_column(String(4))

    # 📞 Contact Info
    contact_number : Mapped [str] = mapped_column(String(20))
    alternate_number : Mapped [str] = mapped_column(String(20))
    email : Mapped [str] = mapped_column(String(100), unique=True)

    # 🧩 Role (you may switch this to FK later)
    role : Mapped [str] = mapped_column(String, nullable=False)

    # 📊 Status / Flags
    status : Mapped [str] = mapped_column(String)  # could later be Enum

    biometric_enrolled : Mapped [bool] = mapped_column(Boolean, default=False)
    is_onboarded : Mapped [bool] = mapped_column(Boolean, default=False)

    is_subcontractor : Mapped [bool] = mapped_column(Boolean, default=False)
    is_fte : Mapped [bool] = mapped_column(Boolean, default=False)

    is_licensed : Mapped [bool] = mapped_column(Boolean, default=False)
    is_insured : Mapped [bool] = mapped_column(Boolean, default=False)
    is_certified : Mapped [bool] = mapped_column(Boolean, default=False)

    # 📍 Address
    address_id : Mapped [str] = mapped_column(
        String,
        ForeignKey('address.address_id')
    )

    # 📈 Metrics
    average_rating : Mapped [float] = mapped_column(Numeric(3, 2))
    years_experience : Mapped [int] = mapped_column(Integer)

    # 🔍 Compliance Links
    background_check_id : Mapped [str] = mapped_column(
        String,
        ForeignKey('background_check.background_check_id')
    )

    drug_test_id : Mapped [str] = mapped_column(
        String,
        ForeignKey('drug_test.drug_test_id')
    )


    preferred_job_types : Mapped [JSON] = mapped_column(JSON)

    # ----------------------
    # 🔗 Relationships
    # ----------------------

    vendor : Mapped ['Vendor'] = relationship('Vendor', backref='contractors')

    manager : Mapped ['Contractor'] = relationship(
        'Contractor',
        remote_side=[contractor_id],
        backref='subordinates'
    )

    address : Mapped ['Address'] = relationship('Address', backref='contractors')

    background_check : Mapped ['BackgroundCheck'] = relationship(
        'BackgroundCheck',
        backref='contractor',
        uselist=False
    )

    drug_test : Mapped ['DrugTest'] = relationship(
        'DrugTest',
        backref='contractor',
        uselist=False
    )
    