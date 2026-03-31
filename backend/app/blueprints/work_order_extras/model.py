
from app.extensions import db
from app.models.base import BaseModel

class CancelledWorkOrder(BaseModel):
    __tablename__ = 'cancelled_work_orders'

    id = db.Column(db.String, primary_key=True)

    work_order_id = db.Column(db.String, db.ForeignKey('work_orders.work_order_id'))
    vendor_id = db.Column(db.String, db.ForeignKey('vendor.vendor_id'))

    cancellation_reason = db.Column(db.Text)