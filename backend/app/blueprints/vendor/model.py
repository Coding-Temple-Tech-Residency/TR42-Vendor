from datetime import datetime, timezone
import enum
from app.extensions import db
from app.models.base import BaseModel

def utc_now():
    return datetime.now(timezone.utc)


class ComplianceStatus(enum.Enum):
    EXPIRED = "expired"
    INCOMPLETE = "incomplete"
    COMPLETE = "complete"


class Vendor(BaseModel):
    __tablename__ = 'vendor'

    vendor_id = db.Column(db.String, primary_key=True)

    company_name = db.Column(db.String(80), unique=True, nullable=False)
    company_code = db.Column(db.String)

    primary_contact_name = db.Column(db.String, nullable=False)
    contact_email = db.Column(db.String, nullable=False)
    contact_phone = db.Column(db.String, nullable=False)

    status = db.Column(
        db.Enum('active', 'inactive', name='vendor_status'),
        nullable=False
    )

    onboarding = db.Column(db.Boolean, nullable=False)

    compliance_status = db.Column(
        db.Enum('expired', 'incomplete', 'complete', name='compliance_status')
    )

    address_id = db.Column(db.String, db.ForeignKey('address.address_id'))

    address = db.relationship('Address', backref='vendors')