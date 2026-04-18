from app.extensions import db
from app.blueprints.fraud_alerts.model import FraudAlert

class FraudAlertRepository:

    @staticmethod
    def create(alert: FraudAlert):
        db.session.add(alert)
        db.session.commit()
        return alert

    @staticmethod
    def get(alert_id: str):
        return FraudAlert.query.get(alert_id)

    @staticmethod
    def get_all():
        return FraudAlert.query.order_by(FraudAlert.flagged_at.desc()).all()

    @staticmethod
    def update(alert: FraudAlert):
        db.session.commit()
        return alert

    @staticmethod
    def delete(alert: FraudAlert):
        db.session.delete(alert)
        db.session.commit()
