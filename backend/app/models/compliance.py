from server.app.extensions import db

class ComplianceDocument(db.Model):
    __tablename__ = 'compliance_document'
    
    compliance_id = db.Column(db.String(50), primary_key=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.vendor_id'))