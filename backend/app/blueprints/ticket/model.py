from app.extensions import db
from app.models.base import BaseModel

class Ticket(BaseModel):
    __tablename__ = 'ticket'

    ticket_id = db.Column(db.String, primary_key=True)

    work_order_id = db.Column(
        db.String,
        db.ForeignKey('work_orders.work_order_id'),
        nullable=False
    )

    description = db.Column(db.Text, nullable=False)

    assigned_contractor = db.Column(
        db.String,
        db.ForeignKey('contractors.contractor_id')
    )

    priority = db.Column(
        db.Enum('routine', 'urgent', 'emergency', name='priority_status')
    )

    status = db.Column(
        db.Enum('assigned', 'in progress', 'completed', name='ticket_status')
    )

    vendor_id = db.Column(db.String, db.ForeignKey('vendor.vendor_id'))

    start_date = db.Column(db.DateTime, nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)

    notes = db.Column(db.Text)

    anomaly_flag = db.Column(db.Boolean)
    anomaly_reason = db.Column(db.Text)

    # Relationships
    work_order = db.relationship('WorkOrder', backref='tickets')
    contractor = db.relationship('Contractor', backref='tickets')
    vendor = db.relationship('Vendor')