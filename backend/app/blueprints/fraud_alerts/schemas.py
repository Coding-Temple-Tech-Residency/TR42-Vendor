from app.extensions import ma
from app.models.fraud_alerts import FraudAlert


class FraudAlertSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FraudAlert
        load_instance = True


fraud_alert_schema = FraudAlertSchema()
fraud_alerts_schema = FraudAlertSchema(many=True)