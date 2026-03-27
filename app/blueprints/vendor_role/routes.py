from flask import Blueprint, request
from app.extensions import db
from .model import VendorRole
from .schemas import vendor_role_schema, vendor_roles_schema
from app.auth.jwt_middleware import vendor_required

vendor_role_bp = Blueprint("vendor_role", __name__)

@vendor_role_bp.get("/")
@vendor_required
def get_roles():
    roles = VendorRole.query.all()
    return vendor_roles_schema.jsonify(roles)

@vendor_role_bp.post("/")
@vendor_required
def create_role():
    data = request.json
    new_role = vendor_role_schema.load(data)
    db.session.add(new_role)
    db.session.commit()
    return vendor_role_schema.jsonify(new_role), 201
