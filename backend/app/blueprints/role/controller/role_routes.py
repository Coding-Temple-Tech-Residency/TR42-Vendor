from flask import Blueprint, request
from app.blueprints.role.services.role_services import RoleService

role_bp = Blueprint("role", __name__, url_prefix="/role")


@role_bp.get("/")
def get_roles():
    return RoleService.get_all(), 200


@role_bp.get("/<role_id>")
def get_role(role_id):
    result = RoleService.get_by_id(role_id)
    if not result:
        return {"message": "Role not found"}, 404
    return result, 200


@role_bp.post("/")
def create_role():
    created = RoleService.create(request.json)
    return created, 201


@role_bp.put("/<role_id>")
def update_role(role_id):
    updated = RoleService.update(role_id, request.json)
    if not updated:
        return {"message": "Role not found"}, 404
    return updated, 200


@role_bp.delete("/<role_id>")
def delete_role(role_id):
    deleted = RoleService.delete(role_id)
    if not deleted:
        return {"message": "Role not found"}, 404
    return {"message": "Deleted"}, 200
