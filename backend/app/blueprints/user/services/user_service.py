from werkzeug.exceptions import BadRequest
from app.extensions import db

from app.blueprints.user.model import User
from app.blueprints.user.repositories.user_repository import UserRepository

# from app.blueprints.user.security import (
#     verify_password,
#     create_token,
#     hash_password,
# )
from logging import getLogger


logger = getLogger(__name__)


class UserService:

    # @staticmethod
    # def login(data: dict):
    #     logger.info("Attempting login for user: %s", data.get("username"))
    #     username = data.get("username")
    #     password = data.get("password")

    #     if not username or not password:
    #         logger.warning("Login failed: Missing username or password")
    #         raise BadRequest("Username and password are required")

    #     user = UserRepository.get_by_username(username)
    #     if not user:
    #         logger.warning("Login failed: Invalid username or password")
    #         raise BadRequest("Invalid username or password")

    #     if not verify_password(password, user.password):
    #         logger.warning("Login failed: Invalid username or password")
    #         raise BadRequest("Invalid username or password")

    #     token = create_token(user)
    #     logger.info("Login successful for user: %s  and token: %s", username, token)

    #     return {
    #         "message": "Login successful",
    #         "token": token,
    #         "user_id": user.user_id,
    #         "username": user.username,
    #         "email": user.email,
    #         "type": user.type,
    #         "is_admin": user.is_admin,
    #     }
    # logger.info("Returning login response for user: %s", username)

    # @staticmethod
    # def get_all():
    #     return UserRepository.get_all()

    # @staticmethod
    # def get(user_id: str):
    #     return UserRepository.get_by_id(user_id)

    @staticmethod
    def create_user(data: dict) -> User:
        password = data.pop("password")

        existing_email = UserRepository.get_by_email(data["email"])
        if existing_email:
            raise ValueError("Email already exists")

        existing_username = UserRepository.get_by_username(data["username"])
        if existing_username:
            raise ValueError("Username already exists")

        user = User(**data)
        user.set_password(password)

        return UserRepository.create(user)

    # @staticmethod
    # def update(user_id: str, data: dict):
    #     user = UserRepository.get_by_id(user_id)
    #     if not user:
    #         return None
    #     return UserRepository.update(user, data)

    # @staticmethod
    # def delete(user_id: str):
    #     user = UserRepository.get_by_id(user_id)
    #     if not user:
    #         return None
    #     UserRepository.delete(user)
    #     return True
