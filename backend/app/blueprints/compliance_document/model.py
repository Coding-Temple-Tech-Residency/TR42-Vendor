from app.extensions import db
from app.models.base import BaseModel

class BackgroundCheck(BaseModel):
    __tablename__ = 'background_check'

    id = db.Column(db.String, primary_key=True)

    background_check_passed = db.Column(db.Boolean)
    background_check_date = db.Column(db.DateTime)
    background_check_provider = db.Column(db.String)


class DrugTest(BaseModel):
    __tablename__ = 'drug_test'

    id = db.Column(db.String, primary_key=True)

    drug_test_passed = db.Column(db.Boolean)
    drug_test_date = db.Column(db.DateTime)


class ComplianceDocument(BaseModel):
    __tablename__ = 'compliance_document'

    id = db.Column(db.String, primary_key=True)

    vendor_id = db.Column(db.String, db.ForeignKey('vendor.id'))

    compliance_document = db.Column(db.LargeBinary)
    compliance_status = db.Column(db.Boolean, default=False)
    expiration_date = db.Column(db.DateTime)

    vendor = db.relationship('Vendor', backref='compliance_documents')

class DriversLicense(BaseModel):
    __tablename__ = 'drivers_license'

    id = db.Column(db.String, primary_key=True)

    license_number = db.Column(db.String)
    expiration_date = db.Column(db.DateTime)