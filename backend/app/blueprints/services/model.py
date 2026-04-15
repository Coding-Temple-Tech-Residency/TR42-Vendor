from app.extensions import db
from app.base import BaseModel

class Service(BaseModel):
    __tablename__ = 'services'

    id = db.Column(db.String, primary_key=True)

    service = db.Column(db.String)

    # relationships
    vendors = db.relationship(
        'VendorService',
        back_populates='service',
        cascade='all, delete-orphan'
    )

class VendorService(db.Model):
    __tablename__ = 'vendor_services'

    id = db.Column(db.String, primary_key=True)

    vendor_id = db.Column(
        db.String,
        db.ForeignKey('vendor.id')
    )

    service_id = db.Column(
        db.String,
        db.ForeignKey('services.id')
    )

    # relationships
    vendor = db.relationship('Vendor', backref='services_link')
    service = db.relationship('Service', back_populates='vendors')