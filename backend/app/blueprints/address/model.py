from app.extensions import db
from app.models.base import BaseModel

class Address(BaseModel):
    __tablename__ = 'address'

    address_id = db.Column(db.String, primary_key=True)

    street = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String(20))
    zipcode = db.Column(db.String(10))
    country = db.Column(db.String(2))