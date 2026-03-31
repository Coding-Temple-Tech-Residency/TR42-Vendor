
from app.extensions import db
from app.models.base import BaseModel
from sqlalchemy import func

class CancelledWorkOrder(BaseModel):
    __tablename__ = 'cancelled_work_orders'

    id = db.Column(db.String, primary_key=True)

    work_order_id = db.Column(
        db.String,
        db.ForeignKey('work_orders.work_order_id'),
        nullable=False
    )

    vendor_id = db.Column(
        db.String,
        db.ForeignKey('vendor.vendor_id'),
        nullable=False
    )

    cancellation_reason = db.Column(db.Text, nullable=False)

    # audit
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())

    created_by = db.Column(
        db.String,
        db.ForeignKey('user.user_id'),
        nullable=False
    )

    updated_by = db.Column(
        db.String,
        db.ForeignKey('user.user_id')
    )

    # relationships
    work_order = db.relationship('WorkOrder', backref='cancellations')
    vendor = db.relationship('Vendor', backref='cancelled_work_orders')