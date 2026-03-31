from server.app.extensions import db
from datetime import datetime

class WorkOrder(db.Model):
    __tablename__ = 'work_order'
    
    work_order_id = db.Column(db.String(50), primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    assigned_vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.vendor_id'))
    well_id = db.Column(db.Integer, db.ForeignKey('well.well_id'))