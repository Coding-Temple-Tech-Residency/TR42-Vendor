from app.extensions import db
from app.models.base import BaseModel

class Service(BaseModel):
    __tablename__ = 'services'

    service_id = db.Column(db.String, primary_key=True)

    service = db.Column(db.String)

    # relationships
    vendors = db.relationship(
        'VendorService',
        back_populates='service',
        cascade='all, delete-orphan'
    )