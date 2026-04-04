from flask import Blueprint, request, jsonify
from ..services.user_service import UserService
from ..schemas import user_schema, users_schema
import logging

user_bp = Blueprint("user_bp", __name__)

# Logging setup
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# -----------------------
# LOGIN
# -----------------------
@user_bp.post("/login")
def login_user():
    try:
        data = request.get_json()
        result = UserService.login(data)
        return result, 200
    except Exception as e:
        logger.exception("Login failed")
        return jsonify({"error": str(e)}), 500


# -----------------------
# CREATE USER
# -----------------------
@user_bp.post("/")
def create_user():
    try:
        data = request.get_json()
        user = UserService.create(data)
        return user_schema.dump(user), 201
    except Exception as e:
        logger.exception("Failed to create user")
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