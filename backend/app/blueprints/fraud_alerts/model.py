from app.extensions import db
from app.models.base import BaseModel

class FraudAlert(BaseModel):
    __tablename__ = 'fraud_alerts'

    id = db.Column(db.String, primary_key=True)

    work_order_id = db.Column(
        db.String,
        db.ForeignKey('work_orders.id')
    )

    ticket_id = db.Column(
        db.String,
        db.ForeignKey('ticket.id')
    )

    severity = db.Column(db.String(100))
    description = db.Column(db.Text)
    status = db.Column(db.String)

    flagged_at = db.Column(db.DateTime)

    # relationships
    work_order = db.relationship('WorkOrder', backref='fraud_alerts')
    ticket = db.relationship('Ticket', backref='fraud_alerts')