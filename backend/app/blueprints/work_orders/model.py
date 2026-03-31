from app.extensions import db
from app.models.base import BaseModel

class WorkOrder(BaseModel):
    __tablename__ = 'work_orders'

    work_order_id = db.Column(db.String, primary_key=True)

    assigned_vendor = db.Column(db.String, db.ForeignKey('vendor.vendor_id'))

    description = db.Column(db.String(500))

    current_status = db.Column(
        db.Enum(
            'unassigned', 'assigned', 'in progress',
            'completed', 'halted', 'rejected',
            name='order_status'
        ),
        nullable=False
    )

    priority = db.Column(
        db.Enum('routine', 'urgent', 'emergency', name='priority_status'),
        nullable=False
    )

    vendor = db.relationship('Vendor', backref='work_orders')