from app.extensions import db
from app.base import BaseModel

class Invoice(db.Model):
    __tablename__ = 'invoice'

    invoice_id = db.Column(db.String, primary_key=True)

    work_order_id = db.Column(db.String, db.ForeignKey('work_orders.work_order_id'))
    ticket_id = db.Column(db.String, db.ForeignKey('ticket.ticket_id'))
    vendor_id = db.Column(db.String, db.ForeignKey('vendor.vendor_id'))

    total_amount = db.Column(db.Numeric)

    invoice_status = db.Column(
        db.Enum('accepted', 'pending', 'rejected', name='invoice_status')
    )