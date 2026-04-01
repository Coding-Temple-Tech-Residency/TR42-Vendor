from app.extensions import db
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import JSON, Interval, Numeric
from app.models.base import BaseModel

class WorkOrder(BaseModel):
    __tablename__ = 'work_orders'

    work_order_id = db.Column(db.String, primary_key=True)

    assigned_vendor = db.Column(
        db.String,  # ⚠️ FIXED (was integer)
        db.ForeignKey('vendor.vendor_id')
    )

    assigned_at = db.Column(db.DateTime)
    completed_at = db.Column(db.DateTime)

    description = db.Column(db.String(500))

    due_date = db.Column(db.DateTime)

    current_status = db.Column(db.String, nullable=False)
    priority = db.Column(db.String, nullable=False)

    comments = db.Column(db.String(500))
    location = db.Column(db.String(60))

    estimated_cost = db.Column(Numeric)
    estimated_duration = db.Column(Interval)

    well_id = db.Column(
        db.String,
        db.ForeignKey('well.well_id')
    )

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

    vendor = db.relationship('Vendor', backref='work_orders')

    well = db.relationship('Well', backref='work_orders')

    creator = db.relationship('User', foreign_keys=[created_by])
    updater = db.relationship('User', foreign_keys=[updated_by])