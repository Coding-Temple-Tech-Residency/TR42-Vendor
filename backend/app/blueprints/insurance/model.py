from app.extensions import db
from app.base import BaseModel

class Insurance(BaseModel):

    __tablename__ = 'insurance'

    id = db.Column(db.String, primary_key=True)
    contractor_id = db.Column(
        db.String,
        db.ForeignKey('contractors.id'),
        nullable=False
    )
    insurance_type = db.Column(db.String, nullable=False)
    policy_number = db.Column(db.Integer, nullable=False)
    provider_name = db.Column(db.String, nullable=False)
    provider_phone = db.Column(db.String, nullable=False)
    coverage_amount = db.Column(db.Numeric)
    deductible = db.Column(db.Numeric)
    effective_date = db.Column(db.DateTime)
    expiration_date = db.Column(db.DateTime)
    insurance_document_url = db.Column(db.String(100))
    insurance_verified = db.Column(db.Boolean, default=False)
    additional_insurance_required = db.Column(db.Boolean)
    additional_insured_certificate_url = db.Column(db.String(100))
