from app.extensions import db
from app.models import BaseModel
from sqlalchemy import JSON

class MSA(BaseModel):
    __tablename__ = 'msa'

    msa_id = db.Column(db.String, primary_key=True)

    vendor_id = db.Column(
        db.String,
        db.ForeignKey('vendor.vendor_id'),
        nullable=False
    )

    version = db.Column(db.String(10))

    effective_date = db.Column(db.DateTime)
    expiration_date = db.Column(db.DateTime)

    status = db.Column(db.String(15))

    uploaded_by = db.Column(
        db.String,
        db.ForeignKey('user.user_id')
    )

    # relationships
    vendor = db.relationship('Vendor', backref='msas')
    uploader = db.relationship('User', foreign_keys=[uploaded_by])


class MSARequirement(BaseModel):
    __tablename__ = 'msa_requirements'

    id = db.Column(db.String, primary_key=True)

    msa_id = db.Column(
        db.String,
        db.ForeignKey('msa.msa_id'),
        nullable=False
    )

    category = db.Column(db.String(50))
    rule_type = db.Column(db.String(50))

    description = db.Column(db.Text)
    value = db.Column(db.String(100))
    unit = db.Column(db.String(100))

    source_field_id = db.Column(db.String)
    page_number = db.Column(db.Integer)

    extracted_text = db.Column(db.Text)
    confidence_score = db.Column(db.Float)

    metadata = db.Column(JSON)

    # relationships
    msa = db.relationship('MSA', backref='requirements')