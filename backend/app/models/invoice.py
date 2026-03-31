from server.app.extensions import db
from datetime import datetime

class Invoice(db.Model):
    __tablename__ = 'invoice'
    
    invoice_id = db.Column(db.String(50), primary_key=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.vendor_id'))
    work_order_id = db.Column(db.String(50), db.ForeignKey('work_order.work_order_id'))


class LineItem(db.Model):
    __tablename__ = 'line_item'
    
    line_item_id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.String(50), db.ForeignKey('invoice.invoice_id'))