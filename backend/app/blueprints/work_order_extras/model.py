
from app.extensions import db
from app.base import BaseModel
from sqlalchemy import func

class CancelledWorkOrder(BaseModel):
    __tablename__ = 'cancelled_work_orders'

    id = db.Column(
        db.String,
        db.ForeignKey('work_orders.id'),
        nullable=False
    )

    vendor_id = db.Column(
        db.String,
        db.ForeignKey('vendor.id'),
        nullable=False
    )

    cancellation_reason = db.Column(db.Text, nullable=False)

    created_by = db.Column(
        db.String,
        db.ForeignKey('user.id'),
        nullable=False
    )

    updated_by = db.Column(
        db.String,
        db.ForeignKey('user.id')
    )

    # relationships
    work_order = db.relationship('WorkOrder', backref='cancellations')
    vendor = db.relationship('Vendor', backref='cancelled_work_orders')