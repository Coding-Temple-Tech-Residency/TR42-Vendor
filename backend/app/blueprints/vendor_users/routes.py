from flask import Blueprint, request
from .vendor_users_service import VendorUserService
from .schemas import vendor_user_schema, vendor_users_schema

vendor_user_bp = Blueprint("vendor_user", __name__)


@vendor_user_bp.post("/assign")
def assign_user():
    data = request.get_json()
    link = VendorUserService.assign_user(data)
    return vendor_user_schema.dump(link), 201


@vendor_user_bp.get("/vendor/<string:vendor_id>")
def get_users_for_vendor(vendor_id):
    links = VendorUserService.get_users_for_vendor(vendor_id)
    return vendor_users_schema.dump(links), 200


@vendor_user_bp.get("/user/<string:user_id>")
def get_vendors_for_user(user_id):
    links = VendorUserService.get_vendors_for_user(user_id)
    return vendor_users_schema.dump(links), 200


@vendor_user_bp.delete("/<string:link_id>")
def delete_link(link_id):
    deleted = VendorUserService.delete_link(link_id)
    if not deleted:
        return {"error": "Link not found"}, 404
    return {"message": "Link deleted"}, 200