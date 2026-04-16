from app.extensions import ma
from app.blueprints.fraud_alerts.model import FraudAlert



class FraudAlertSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FraudAlert
        load_instance = True
        include_fk = True


alert_schema = FraudAlertSchema()
alerts_schema = FraudAlertSchema(many=True)