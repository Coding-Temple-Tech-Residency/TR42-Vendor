from app.extensions import db

class Address(db.Model):
    __tablename__ = "addresses"

    address_id = db.Column(db.String, primary_key=True)
    street = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String(20))
    zip = db.Column(db.String(10))
    country = db.Column(db.String(2))
