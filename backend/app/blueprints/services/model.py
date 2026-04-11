from app.extensions import db


class Service(db.Model):
    __tablename__ = 'services'

    service_id = db.Column(db.String, primary_key=True)

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
        db.ForeignKey('vendor.vendor_id')
    )

    service_id = db.Column(
        db.String,
        db.ForeignKey('services.service_id')
    )

    # relationships
    vendor = db.relationship('Vendor', backref='services_link')
    service = db.relationship('Service', backref='vendor_links')