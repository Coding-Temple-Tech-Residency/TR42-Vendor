from server.app.extensions import db

class VendorRole(db.Model):
    __tablename__ = 'vendor_role'
    
    vendor_role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(20), nullable=False)


class ClientRole(db.Model):
    __tablename__ = 'client_role'
    
    client_role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(20), nullable=False)


class ContractorRole(db.Model):
    __tablename__ = 'contractor_role'
    
    contractor_role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(20), nullable=False)