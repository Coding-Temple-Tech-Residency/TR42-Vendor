from flask import Blueprint, jsonify, make_response, request
from sqlalchemy import select
from werkzeug.exceptions import BadRequest
from marshmallow import ValidationError
from app.extensions import db
from app.blueprints.vendor_user.model import VendorUserRole
from app.blueprints.user.schemas import user_schema, users_schema
from app.blueprints.user.services.user_services import UserService
from app.auth.tokens import (
    token_required,
    vendor_membership_required,
    vendor_roles_required,
)
from app.blueprints.user.model import User
import logging


logger = logging.getLogger(__name__)

user_bp = Blueprint("user_bp", __name__)


@user_bp.post("/login")
def login_user():
    data = request.get_json()
    logger.debug("User login attempt")

    if not data:
        return jsonify({"error": "No input data provided"}), 400

    try:
        result = UserService.login(data)
        token = result.pop("token")

        response = make_response(jsonify(result), 200)
        response.set_cookie(
            "access_token",
            token,
            httponly=True,
            secure=True,
            samesite="Lax",
            max_age=3600,
        )
        return response

    except BadRequest as err:
        return jsonify({"error": err.description}), 400

    except Exception:
        logger.exception("Error during login")
        return jsonify({"error": "An error occurred during login"}), 500


@user_bp.post("/")
def create_user():
    data = request.get_json()
    logger.debug("Creating a new user")

    if not data:
        logger.warning("No input data provided for user creation")
        return jsonify({"error": "No input data provided"}), 400

    try:
        validated_data = user_schema.load(data)
        logger.debug("User data validated successfully")

        new_user = UserService.create_user(validated_data)
        logger.info(
            "User created successfully: %s %s",
            new_user.first_name,
            new_user.last_name,
        )

        return jsonify(user_schema.dump(new_user)), 201

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    except ValueError as err:
        return jsonify({"error": str(err)}), 400

    except Exception:
        logger.exception("Error creating user")
        return jsonify({"error": "An error occurred while creating user"}), 500


@user_bp.get("/")
@token_required
def get_all_users(current_user):
    if not current_user.is_admin:
        return jsonify({"message": "Forbidden"}), 403

    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=10, type=int)

    result = UserService.get_all_paginated(page=page, per_page=per_page)
    return jsonify(result), 200


@user_bp.get("/vendor/users")
@token_required
@vendor_membership_required
@vendor_roles_required([VendorUserRole.ADMIN, VendorUserRole.MANAGER])
def get_vendor_users(current_user, vendor_link, vendor_id):
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=10, type=int)

    result = UserService.get_vendor_users_paginated(
        vendor_id=vendor_id,
        page=page,
        per_page=per_page,
    )
    return jsonify(result), 200


# -----------------------
# GET LOGGED IN USER
# -----------------------
@user_bp.get("/profile")
@token_required
def get_logged_in_user(user, user_role):
    try:
        # User is already fetched and passed by the middleware
        return user_schema.dump(user), 200
    except Exception as e:
        logger.exception("Failed to fetch logged-in user")
        return jsonify({"error": str(e)}), 500


# -----------------------
# GET ALL USERS
# -----------------------
@user_bp.get("/")
def get_users():
    try:
        users = UserService.get_all()
        return users_schema.dump(users), 200
    except Exception as e:
        logger.exception("Failed to fetch users")
        return jsonify({"error": str(e)}), 500


# -----------------------
# GET SINGLE USER
# -----------------------
@user_bp.get("/<user_id>")
def get_user(user_id):
    try:
        user = UserService.get_by_id(user_id)

        if not user:
            return jsonify({"error": "User not found"}), 404

        return user_schema.dump(user), 200
    except Exception as e:
        logger.exception(f"Failed to fetch user {user_id}")
        return jsonify({"error": str(e)}), 500


# -----------------------
# UPDATE USER
# -----------------------
@user_bp.put("/<user_id>")
def update_user(user_id):
    try:
        data = request.get_json()
        user = UserService.get_by_id(user_id)

        if not user:
            return jsonify({"error": "User not found"}), 404

        updated_user = UserService.update(user, data)
        return user_schema.dump(updated_user), 200
    except Exception as e:
        logger.exception(f"Failed to update user {user_id}")
        return jsonify({"error": str(e)}), 500


# -----------------------
# DELETE USER
# -----------------------
@user_bp.delete("/<user_id>")
def delete_user(user_id):
    try:
        user = UserService.get_by_id(user_id)

        if not user:
            return jsonify({"error": "User not found"}), 404

        UserService.delete(user)
        return jsonify({"message": "User deleted"}), 200
    except Exception as e:
        logger.exception(f"Failed to delete user {user_id}")
        return jsonify({"error": str(e)}), 500
