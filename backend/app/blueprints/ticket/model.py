from app.extensions import db
from sqlalchemy import func
from app.base import BaseModel


class Ticket(BaseModel):
    __tablename__ = 'ticket'

    ticket_id = db.Column(db.String, primary_key=True)

    invoice_id = db.Column(
        db.String,
        db.ForeignKey('invoice.invoice_id'),
        nullable=True
    )

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

    vendor_id = db.Column(
        db.String,
        db.ForeignKey('vendor.vendor_id')
    )

    priority = db.Column(db.String)
    status = db.Column(db.String)

    start_date = db.Column(db.DateTime, nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)

    estimated_duration = db.Column(db.Interval)

    notes = db.Column(db.Text)

    # ⚠️ FIX: geography → use Float unless you enable PostGIS
    contractor_start_lat = db.Column(db.Float)
    contractor_start_lng = db.Column(db.Float)

    contractor_end_lat = db.Column(db.Float)
    contractor_end_lng = db.Column(db.Float)

    estimated_quantity = db.Column(db.Integer)
    unit = db.Column(db.String)

    special_requirements = db.Column(db.Text)

    anomaly_flag = db.Column(db.Boolean, default=False)
    anomaly_reason = db.Column(db.Text)

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

    # ----------------------
    # 🔗 Relationships
    # ----------------------

    work_order = db.relationship('WorkOrder', backref='tickets')

    contractor = db.relationship('Contractor', backref='tickets')

    vendor = db.relationship('Vendor', backref='tickets')

    creator = db.relationship('User', foreign_keys=[created_by])
    updater = db.relationship('User', foreign_keys=[updated_by])