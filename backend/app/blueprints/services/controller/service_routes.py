from flask import Blueprint, request
from app.blueprints.services.services.service_services import ServiceService
from app.blueprints.services.schemas import service_schema, services_schema



services_bp = Blueprint("services", __name__)

@services_bp.post("/")
def create_service():
    data = request.get_json()
    service = ServiceService.create(data)
    return service_schema.dump(service), 201

@services_bp.get("/")
def get_all_services():
    return services_schema.dump(ServiceService.get_all()), 200

@services_bp.get("/<service_id>")
def get_service(service_id):
    service = ServiceService.get(service_id)
    if not service:
        return {"error": "Service not found"}, 404
    return service_schema.dump(service), 200


@services_bp.put("/<service_id>")
def update_service(service_id):
    service = ServiceService.get(service_id)
    if not service:
        return {"error": "Service not found"}, 404

    data = request.get_json()
    updated = ServiceService.update(service, data)
    return service_schema.dump(updated), 200


@services_bp.delete("/<service_id>")
def delete_service(service_id):
    service = ServiceService.get(service_id)
    if not service:
        return {"error": "Service not found"}, 404

    ServiceService.delete(service)
    return {"message": "Service deleted"}, 200
