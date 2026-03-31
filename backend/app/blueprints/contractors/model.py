from app.extensions import db
from app.models.base import BaseModel

class Contractor(BaseModel):
    __tablename__ = 'contractors'

    contractor_id = db.Column(db.String, primary_key=True)

    employee_number = db.Column(db.String, nullable=False)

    vendor_id = db.Column(db.String, db.ForeignKey('vendor.vendor_id'), nullable=False)

    contact_number = db.Column(db.String(20))
    alternate_number = db.Column(db.String(20))

    email = db.Column(db.String(100), unique=True)

    role_id = db.Column(db.String,db.ForeignKey('role.role_id'))

    role = db.relationship('Role')

    status = db.Column(
        db.Enum('active', 'inactive', name='contractor_status')
    )

    address_id = db.Column(db.String, db.ForeignKey('address.address_id'))

    vendor = db.relationship('Vendor', backref='contractors')
    address = db.relationship('Address', backref='contractors')