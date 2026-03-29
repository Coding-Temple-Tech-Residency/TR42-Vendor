from server.app.extensions import db

class VendorUser(db.Model):
    __tablename__ = 'vendor_user'
    vendor_user_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.vendor_id'))
    vendor_role_id = db.Column(db.Integer, db.ForeignKey('vendor_role.vendor_role_id'))


class ClientUser(db.Model):
    __tablename__ = 'client_user'
    client_user_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    client_role_id = db.Column(db.Integer, db.ForeignKey('client_role.client_role_id'))


class VendorService(db.Model):
    __tablename__ = 'vendor_service'
    vendor_service_id = db.Column(db.Integer, primary_key=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.vendor_id'))
    service_id = db.Column(db.Integer, db.ForeignKey('service.service_id'))


class VendorWell(db.Model):
    __tablename__ = 'vendor_well'
    vendor_well_id = db.Column(db.Integer, primary_key=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.vendor_id'))
    well_id = db.Column(db.Integer, db.ForeignKey('well.well_id'))