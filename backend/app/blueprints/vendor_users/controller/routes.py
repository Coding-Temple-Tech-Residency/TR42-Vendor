from flask import Blueprint, request
from ..services.vendor_users_service import VendorUserService
from ..schemas import vendor_user_schema, vendor_users_schema
import logging

logger = logging.getLogger(__name__)

vendor_user_bp = Blueprint("vendor_user", __name__)


"""
Handles GET requests to the root endpoint of the vendor user blueprint.
Retrieves all vendor users using the VendorUserService and returns them serialized as JSON.

Returns:
    Response: A JSON response containing a list of all vendor users.
"""


@vendor_user_bp.get("/")
def get_vendor_users():
    try:
        logger.debug("Fetching all vendor users")
        users = VendorUserService.get_all_users()
        logger.info(f"Retrieved {len(users)} users")
        return vendor_users_schema.jsonify(users), 200
    except Exception as e:
        logger.error(f"Error fetching users: {str(e)}")
        return {"error": "An error occurred while fetching users"}, 500




"""
Create a new vendor user.

This endpoint handles POST requests to create a new vendor user with the provided data.
The request body should contain JSON  with the vendor user information.

Returns:
    tuple: A tuple containing:
        - dict: Serialized vendor user object in JSON format
        - int: HTTP status code 201 (Created)

Raises:
    BadRequest: If the request body is invalid or missing required fields
    ValidationError: If the provided data fails validation
"""


@vendor_user_bp.post("/")
def create_vendor_user():
    try:
        logger.debug("Creating a new vendor user")
        data = request.get_json()
        logger.info(f"Received vendor user data: {data}")
        new_user = VendorUserService.create_user(data)
        logger.info(f"Created vendor user in repo: {new_user.id}")
        return vendor_user_schema.jsonify(new_user), 201
    except Exception as e:
        logger.error(f"POST /vendor_user/ - Error creating user: {str(e)}")
        return {"error": "An error occurred while creating the user"}, 500