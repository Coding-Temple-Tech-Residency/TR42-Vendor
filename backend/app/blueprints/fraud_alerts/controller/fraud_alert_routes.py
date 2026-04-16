from flask import Blueprint, request
from app.blueprints.fraud_alerts.services.fraud_alert_services import AlertService
from app.blueprints.fraud_alerts.repositories.fraud_alert_repositories import FraudAlertRepository
from app.blueprints.fraud_alerts.schemas import alert_schema, alerts_schema

alerts_bp = Blueprint("alerts", __name__)

# Create alert
@alerts_bp.post("/")
def create_alert():
    data = request.get_json()

    alert = AlertService.create_alert(data)
    return alert_schema.dump(alert), 201



# Get all alerts
@alerts_bp.get("/")
def get_alerts():
    alerts = FraudAlertRepository.get_all()
    return alerts_schema.dump(alerts), 200


# Get alert by ID
@alerts_bp.get("/<alert_id>")
def get_alert(alert_id):
    alert = FraudAlertRepository.get(alert_id)
    if not alert:
        return {"message": "Alert not found"}, 404
    return alert_schema.dump(alert), 200


# Resolve alert
#Resolve = real issue, fixed
@alerts_bp.put("/<alert_id>/resolve")
def resolve_alert(alert_id):
    alert = FraudAlertRepository.get(alert_id)
    if not alert:
        return {"message": "Alert not found"}, 404

    user_id = request.json.get("user_id")
    updated = AlertService.resolve(alert, user_id)
    return alert_schema.dump(updated), 200


# Dismiss alert
#Dismiss = false issue, ignored
@alerts_bp.put("/<alert_id>/dismiss")
def dismiss_alert(alert_id):
    alert = FraudAlertRepository.get(alert_id)
    if not alert:
        return {"message": "Alert not found"}, 404

    user_id = request.json.get("user_id")
    updated = AlertService.dismiss(alert, user_id)
    return alert_schema.dump(updated), 200
