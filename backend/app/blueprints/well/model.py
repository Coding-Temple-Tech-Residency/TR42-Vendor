from app.extensions import db
from app.models.base import BaseModel

class Well(BaseModel):
    __tablename__ = 'well'

    well_id = db.Column(db.String, primary_key=True)

    api_number = db.Column(db.String)
    well_name = db.Column(db.String)

    status = db.Column(db.String)
    type = db.Column(db.String)


class WellLocation(BaseModel):
    __tablename__ = 'well_location'

    well_location_id = db.Column(db.String, primary_key=True)

    well_id = db.Column(db.String, db.ForeignKey('well.well_id'))

    well = db.relationship('Well', backref='locations')


class VendorWell(BaseModel):
    __tablename__ = 'vendor_well'

    id = db.Column(db.String, primary_key=True)

    vendor_id = db.Column(db.String, db.ForeignKey('vendor.vendor_id'))
    well_id = db.Column(db.String, db.ForeignKey('well.well_id'))