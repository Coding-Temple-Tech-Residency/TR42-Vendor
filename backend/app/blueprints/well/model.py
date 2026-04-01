from app.extensions import db
from app.models.base import BaseModel
from sqlalchemy import func

class Well(BaseModel):
    __tablename__ = 'well'

    well_id = db.Column(db.String, primary_key=True)

    api_number = db.Column(db.String)
    well_name = db.Column(db.String)

    status = db.Column(db.String)
    type = db.Column(db.String)


class WellLocation(db.Model):
    __tablename__ = 'well_location'

    well_location_id = db.Column(db.String, primary_key=True)

    well_id = db.Column(
        db.String,
        db.ForeignKey('well.well_id'),
        nullable=False
    )

    # ⚠️ FIX: geography → float (unless using PostGIS)
    surface_latitude = db.Column(db.Float)
    surface_longitude = db.Column(db.Float)

    bottom_latitude = db.Column(db.Float)
    bottom_longitude = db.Column(db.Float)

    county = db.Column(db.String)
    state = db.Column(db.String(2))
    field_name = db.Column(db.String)

    section = db.Column(db.Integer)
    township = db.Column(db.String(2))

    # audit
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())

    created_by = db.Column(
        db.String,
        db.ForeignKey('user.user_id'),
        nullable=False
    )

    updated_by = db.Column(
        db.String,
        db.ForeignKey('user.user_id')
    )

    # relationships
    well = db.relationship('Well', backref='locations')


class VendorWell(db.Model):
    __tablename__ = 'vendor_well'

    id = db.Column(db.String, primary_key=True)

    vendor_id = db.Column(
        db.String,
        db.ForeignKey('vendor.vendor_id'),
        nullable=False
    )

    well_id = db.Column(
        db.String,
        db.ForeignKey('well.well_id'),
        nullable=False
    )

    # audit
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())

    created_by = db.Column(
        db.String,
        db.ForeignKey('user.user_id'),
        nullable=False
    )

    updated_by = db.Column(
        db.String,
        db.ForeignKey('user.user_id')
    )

    # relationships
    vendor = db.relationship('Vendor', backref='vendor_wells')
    well = db.relationship('Well', backref='vendor_links')