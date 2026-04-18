from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest

from app.blueprints.fraud_alerts.model import FraudAlert
from app.blueprints.fraud_alerts.repositories.fraud_alert_repositories import FraudAlertRepository
from app.blueprints.fraud_alerts.schemas import alert_schema


class AlertService:

    @staticmethod
    def create_alert(data: dict) -> FraudAlert:
        try:
            # Marshmallow validates and constructs the FraudAlert instance
            alert = alert_schema.load(data)
            return FraudAlertRepository.create(alert)
        except ValidationError as e:
            raise BadRequest(e.messages)

    @staticmethod
    def resolve(alert: FraudAlert, user_id: str) -> FraudAlert:
        try:
            update_data = {
                "status": "RESOLVED",
                "updated_by_user_id": user_id
            }

            updated_alert = alert_schema.load(
                update_data,
                instance=alert,
                partial=True
            )

            return FraudAlertRepository.update(updated_alert)

        except ValidationError as e:
            raise BadRequest(e.messages)

    @staticmethod
    def dismiss(alert: FraudAlert, user_id: str) -> FraudAlert:
        try:
            update_data = {
                "status": "DISMISSED",
                "updated_by_user_id": user_id
            }

            updated_alert = alert_schema.load(
                update_data,
                instance=alert,
                partial=True
            )

            return FraudAlertRepository.update(updated_alert)

        except ValidationError as e:
            raise BadRequest(e.messages)
