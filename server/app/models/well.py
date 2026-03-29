from app.extensions import db

class Well(db.Model):
    __tablename__ = 'well'
    
    well_id = db.Column(db.Integer, primary_key=True)
    api_number = db.Column(db.String(20), unique=True, nullable=False)
    well_name = db.Column(db.String(80), nullable=False)
    operator = db.Column(db.String(80), nullable=False)
    well_status = db.Column(db.String(20), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    
    company_id = db.Column(db.Integer, db.ForeignKey('company.company_id'), nullable=False)


class WellLocation(db.Model):
    __tablename__ = 'well_location'
    
    well_location_id = db.Column(db.Integer, primary_key=True)
    surface_latitude = db.Column(db.Float, nullable=False)
    surface_longitude = db.Column(db.Float, nullable=False)

    well_id = db.Column(db.Integer, db.ForeignKey('well.well_id'), nullable=False)