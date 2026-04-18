from flask import Blueprint, request
from app.blueprints.msa.services.msa_services import MSAService
from app.blueprints.msa.repositories.msa_repositories import MSARepository
from app.blueprints.msa.schemas import msa_schema, msas_schema
import datetime

msa_bp = Blueprint("msa", __name__)


@msa_bp.post("/")
def create_msa():
    msa = MSAService.create(request.json)
    return msa_schema.dump(msa), 201


@msa_bp.get("/")
def get_all_msas():
    return msas_schema.dump(MSARepository.get_all()), 200


@msa_bp.get("/<msa_id>")
def get_msa(msa_id):
    msa = MSARepository.get(msa_id)
    if not msa:
        return {"message": "Not found"}, 404
    return msa_schema.dump(msa), 200


@msa_bp.put("/<msa_id>")
def update_msa(msa_id):
    msa = MSARepository.get(msa_id)
    if not msa:
        return {"message": "Not found"}, 404

    data = request.json

    if "updated_by_user_id" not in data:
        return {"message": "updated_by_user_id is required"}, 400

    updated = MSAService.update(msa, data)
    return msa_schema.dump(updated), 200

@msa_bp.delete("/<msa_id>")
def delete_msa(msa_id):
    msa = MSARepository.get(msa_id)
    if not msa:
        return {"message": "Not found"}, 404

    MSAService.delete(msa)
    return {"message": "Deleted"}, 200
