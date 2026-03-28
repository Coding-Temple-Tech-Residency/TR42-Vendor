from app.extensions import db
from datetime import datetime

class FraudAlert(db.Model):
    __tablename__ = 'fraud_alert'
    
    fraud_alert_id = db.Column(db.String(50), primary_key=True)
    work_order_id = db.Column(db.String(50), db.ForeignKey('work_order.work_order_id'))