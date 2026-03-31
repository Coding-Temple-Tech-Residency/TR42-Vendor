from app.extensions import db
from app.models.base import BaseModel

class VendorUser(BaseModel):
    __tablename__ = 'vendor_user'

    id = db.Column(db.String, primary_key=True)

    user_id = db.Column(db.String, db.ForeignKey('user.user_id'), unique=True)
    vendor_id = db.Column(db.String, db.ForeignKey('vendor.vendor_id'))

    role = db.Column(db.String)


class VendorService(BaseModel):
    __tablename__ = 'vendor_services'

    id = db.Column(db.String, primary_key=True)

    vendor_id = db.Column(
        db.String,
        db.ForeignKey('vendor.vendor_id'),
        nullable=False
    )

    service_id = db.Column(
        db.String,
        db.ForeignKey('services.service_id'),
        nullable=False
    )

    # relationships
    vendor = db.relationship('Vendor', backref='vendor_services')
    service = db.relationship('Service', back_populates='vendors')