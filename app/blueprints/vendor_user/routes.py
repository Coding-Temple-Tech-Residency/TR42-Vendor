from flask import Blueprint, request
from app.extensions import db
from .model import VendorUser
from .schemas import vendor_user_schema, vendor_users_schema

from app.auth.jwt_middleware import vendor_required




vendor_user_bp = Blueprint("vendor_user", __name__)

@vendor_user_bp.get("/")
@vendor_required
def get_vendor_users():
    users = VendorUser.query.all()
    return vendor_users_schema.jsonify(users)

@vendor_user_bp.post("/")
@vendor_required
def create_vendor_user():
    data = request.json
    new_user = vendor_user_schema.load(data)
    db.session.add(new_user)
    db.session.commit()
    return vendor_user_schema.jsonify(new_user), 201



