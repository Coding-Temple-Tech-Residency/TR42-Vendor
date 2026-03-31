from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from app.blueprints.vendors.model import Vendor
from app.blueprints.vendors.services.vendors_service import VendorService
from app.blueprints.vendors.schemas import vendor_schema, vendors_schema
import logging

logger = logging.getLogger(__name__)


vendors_bp = Blueprint("vendors_bp", __name__, url_prefix="/vendors")


@vendors_bp.get("/")
def get_vendors():
    try:
        logger.debug("Fetching all vendors")
        vendors = VendorService.get_all_vendors()
        logger.info(f"Retrieved {len(vendors)} vendors")
        return vendors_schema.jsonify(vendors), 200
    except Exception:
        logger.exception("Error fetching vendors")
        return {"error": "An error occurred while fetching vendors"}, 500


@vendors_bp.post("/")
def create_vendor():
    try:
        data = request.get_json()
        logger.debug("Creating a new vendor")
        if not data:
            logger.warning("No input data provided for vendor creation")
            return {"error": "No input data provided"}, 400

        validated_data: Vendor = vendor_schema.load(data)
        logger.debug("Vendor data validated successfully")

        new_vendor: Vendor = VendorService.create_vendor(validated_data)

        logger.info(f"Vendor created successfull: {new_vendor.company_name}")
        return vendor_schema.jsonify(new_vendor), 201
    except ValidationError as err:
        logger.warning(f"Validation error while creating vendor: {err.messages}")
        return {"error": "Validation error", "messages": err.messages}, 400
