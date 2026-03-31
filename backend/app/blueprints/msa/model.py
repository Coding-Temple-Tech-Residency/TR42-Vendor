from app.extensions import db
from app.models.base import BaseModel

class MSA(BaseModel):
    __tablename__ = 'msa'

    msa_id = db.Column(db.String, primary_key=True)
    vendor_id = db.Column(db.String, db.ForeignKey('vendor.vendor_id'))

    version = db.Column(db.String(10))
    status = db.Column(db.String(15))

    vendor = db.relationship('Vendor', backref='msas')


class MSARequirement(BaseModel):
    __tablename__ = 'msa_requirements'

    id = db.Column(db.String, primary_key=True)
    msa_id = db.Column(db.String, db.ForeignKey('msa.msa_id'))

    category = db.Column(db.String)
    rule_type = db.Column(db.String)

    msa = db.relationship('MSA', backref='requirements')