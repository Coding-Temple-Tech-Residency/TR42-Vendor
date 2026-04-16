from flask import Blueprint, request
from app.blueprints.msa_requirements.services.msa_requirements_service import MSARequirementsService
from app.blueprints.msa_requirements.repositories.msa_requirements_repositories import MSARequirementsRepository
from app.blueprints.msa_requirements.schemas import msa_req_schema, msa_reqs_schema

msa_req_bp = Blueprint("msa_requirements", __name__)


@msa_req_bp.post("/<msa_id>")
def create_requirement(msa_id):
    req = MSARequirementsService.create(msa_id, request.json)
    return msa_req_schema.dump(req), 201


@msa_req_bp.get("/<msa_id>")
def get_requirements(msa_id):
    return msa_reqs_schema.dump(
        MSARequirementsRepository.get_by_msa(msa_id)
    ), 200


@msa_req_bp.put("/req/<req_id>")
def update_requirement(req_id):
    req = MSARequirementsRepository.get(req_id)
    if not req:
        return {"message": "Not found"}, 404

    data = request.json

    if "updated_by_user_id" not in data:
        return {"message": "updated_by_user_id is required"}, 400

    updated = MSARequirementsService.update(req, data)
    return msa_req_schema.dump(updated), 200


@msa_req_bp.delete("/req/<req_id>")
def delete_requirement(req_id):
    req = MSARequirementsRepository.get(req_id)
    if not req:
        return {"message": "Not found"}, 404

    MSARequirementsService.delete(req)
    return {"message": "Deleted"}, 200
