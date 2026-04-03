
from werkzeug.exceptions import BadRequest
from ..repositories.user_repository import UserRepository
from app.blueprints.user.utils import verify_password, create_token, hash_password
from logging import getLogger


logger = getLogger(__name__)


class UserService:


    @staticmethod
    def login(data: dict):
        logger.info("Attempting login for user: %s", data.get("username"))
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            logger.warning("Login failed: Missing username or password")
            raise BadRequest("Username and password are required")

        user = UserRepository.get_by_username(username)
        if not user:
            logger.warning("Login failed: Invalid username or password")
            raise BadRequest("Invalid username or password")

        if not verify_password(password, user.password):
            logger.warning("Login failed: Invalid username or password")
            raise BadRequest("Invalid username or password")

        token = create_token(user)
        logger.info("Login successful for user: %s  and token: %s", username, token)

        return {
            "message": "Login successful",
            "token": token,
            "user_id": user.user_id,
            "username": user.username,
            "email": user.email,
            "type": user.type,
            "is_admin": user.is_admin
        }
        logger.info("Returning login response for user: %s", username)

    # @staticmethod
    # def get_all():
    #     return UserRepository.get_all()

    # @staticmethod
    # def get(user_id: str):
    #     return UserRepository.get_by_id(user_id)

    @staticmethod
    def create(data: dict):

        # Hash the password BEFORE saving
        data["password"] = hash_password(data["password"])

        return UserRepository.create(data)

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