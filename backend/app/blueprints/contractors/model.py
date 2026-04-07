from app.extensions import db
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import Numeric
from app.base import BaseModel


class Contractor(BaseModel):
    __tablename__ = 'contractors'

    contractor_id = db.Column(db.String, primary_key=True)

    employee_number = db.Column(db.String, nullable=False)

    vendor_id = db.Column(
        db.String,
        db.ForeignKey('vendor.vendor_id'),
        nullable=False
    )

    vendor_manager_id = db.Column(
        db.String,
        db.ForeignKey('contractors.contractor_id'),
        nullable=True  # allow null for top-level managers
    )

    # 🧑 Personal Info
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    middle_name = db.Column(db.String(80))

    date_of_birth = db.Column(db.DateTime)
    ssn_last_four = db.Column(db.String(4))

    # 📞 Contact Info
    contact_number = db.Column(db.String(20))
    alternate_number = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True)

    # 🧩 Role (you may switch this to FK later)
    role = db.Column(db.String, nullable=False)

    # 📊 Status / Flags
    status = db.Column(db.String)  # could later be Enum

    biometric_enrolled = db.Column(db.Boolean, default=False)
    is_onboarded = db.Column(db.Boolean, default=False)

    is_subcontractor = db.Column(db.Boolean, default=False)
    is_fte = db.Column(db.Boolean, default=False)

    is_licensed = db.Column(db.Boolean, default=False)
    is_insured = db.Column(db.Boolean, default=False)
    is_certified = db.Column(db.Boolean, default=False)

    # 📍 Address
    address_id = db.Column(
        db.String,
        db.ForeignKey('address.address_id')
    )

    # 📈 Metrics
    average_rating = db.Column(Numeric(3, 2))
    years_experience = db.Column(db.Integer)

    # 🔍 Compliance Links
    background_check_id = db.Column(
        db.String,
        db.ForeignKey('background_check.background_check_id')
    )

    drug_test_id = db.Column(
        db.String,
        db.ForeignKey('drug_test.drug_test_id')
    )

    drivers_license_id = db.Column(
        db.String,
        db.ForeignKey('drivers_license.license_id')
    )

    preferred_job_types = db.Column(JSON)

    # ----------------------
    # 🔗 Relationships
    # ----------------------

    vendor = db.relationship('Vendor', backref='contractors')

    manager = db.relationship(
        'Contractor',
        remote_side=[contractor_id],
        backref='subordinates'
    )

    address = db.relationship('Address', backref='contractors')

    background_check = db.relationship(
        'BackgroundCheck',
        backref='contractor',
        uselist=False
    )

    drug_test = db.relationship(
        'DrugTest',
        backref='contractor',
        uselist=False
    )