from app.extensions import db
from datetime import datetime


class Ticket(db.Model):
    __tablename__ = 'ticket'
    
    ticket_id = db.Column(db.Integer, primary_key=True)
    
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300), nullable=True)
    
    status = db.Column(db.String(20), nullable=False, default='open')
    # open, in_progress, completed, blocked
    
    priority = db.Column(db.String(20), nullable=False, default='medium')
    # low, medium, high
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    due_date = db.Column(db.DateTime, nullable=True)
    
    # Relationships
    work_order_id = db.Column(
        db.String(50),
        db.ForeignKey('work_order.work_order_id'),
        nullable=False
    )
    
    assigned_contractor_id = db.Column(
        db.Integer,
        db.ForeignKey('contractor.contractor_id'),
        nullable=True
    )

    # Optional tracking fields
    estimated_hours = db.Column(db.Float, nullable=True)
    actual_hours = db.Column(db.Float, nullable=True)

    # Relationships (ORM side)
    work_order = db.relationship('WorkOrder', backref='tickets')
    contractor = db.relationship('Contractor', backref='tickets')

# class Job(db.Model):
#     __tablename__ = 'job'
    
#     job_id = db.Column(db.String(50), primary_key=True)
#     description = db.Column(db.String(200), nullable=True)
#     priority = db.Column(db.String(20), nullable=False)  # 'low', 'medium', 'high'
#     job_status = db.Column(db.String(20), nullable=False)  # 'open', 'in_progress', 'closed', etc.
#     estimated_duration = db.Column(db.Float, nullable=True)  # in hours
#     start_time = db.Column(db.DateTime, nullable=True)
#     end_time = db.Column(db.DateTime, nullable=True)
#     estimated_quantity = db.Column(db.Float, nullable=True)
#     unit = db.Column(db.String(20), nullable=True)  # 'hours', 'tons', 'barrels', etc.
#     notes = db.Column(db.String(200), nullable=True)  
#     special_requirements = db.Column(db.String(200), nullable=True)
#     contractor_start_location = db.Column(db.String(100), nullable=True)
#     contractor_end_location = db.Column(db.String(100), nullable=True)
#     anomaly_flag = db.Column(db.Boolean, default=False)
#     anomaly_reason = db.Column(db.String(200), nullable=True)
    
#     work_order_id = db.Column(db.String(50), db.ForeignKey('work_order.work_order_id'), nullable=False)
#     assigned_contractor_id = db.Column(db.Integer, db.ForeignKey('contractor.contractor_id'), nullable=True)
    
