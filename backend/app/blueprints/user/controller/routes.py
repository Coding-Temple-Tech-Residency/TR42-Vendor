from flask import Blueprint, jsonify, request
from app.blueprints.user.schemas import user_schema, users_schema
from app.blueprints.user.services.user_service import UserService

import logging

logger = logging.getLogger(__name__)

user_bp = Blueprint("user_bp", __name__)


@user_bp.post("/login")
def login_user():
    data = request.get_json()
    result = UserService.login(data)
    return result, 200


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

    except Exception:
        logger.exception("Error creating user")
        return jsonify({"error": "An error occurred while creating user"}), 500
