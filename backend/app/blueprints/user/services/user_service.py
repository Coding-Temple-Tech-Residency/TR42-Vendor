from werkzeug.exceptions import BadRequest, NotFound
from ..repositories.user_repository import UserRepository
from app.blueprints.user.utils import verify_password, create_token, hash_password
from logging import getLogger

logger = getLogger(__name__)


class UserService:

    # -----------------------
    # LOGIN
    # -----------------------
    @staticmethod
    def login(data: dict):
        logger.info("Attempting login for user: %s", data.get("username"))

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            logger.warning("Login failed: Missing username or password")
            raise BadRequest("Username and password are required")

        user = UserRepository.get_by_username(username)

        if not user or not verify_password(password, user.password):
            logger.warning("Login failed: Invalid username or password")
            raise BadRequest("Invalid username or password")

        token = create_token(user)

        logger.info("Login successful for user: %s", username)

        return {
            "message": "Login successful",
            "token": token,
            "user_id": user.user_id,
            "username": user.username,
            "email": user.email,
            "type": user.type,
            "is_admin": user.is_admin
        }


    # -----------------------
    # CREATE USER
    # -----------------------
    @staticmethod
    def create(data: dict):
        if "password" not in data or not data["password"]:
            raise BadRequest("Password is required")
        
        existing = UserRepository.get_by_username(data["username"])
        if existing:
            raise BadRequest("Username already exists")

        # Hash password
        data["password"] = hash_password(data["password"])

        logger.info("Creating user: %s", data.get("username"))

        return UserRepository.create(data)


    # -----------------------
    # GET ALL USERS
    # -----------------------
    @staticmethod
    def get_all():
        logger.info("Fetching all users")
        return UserRepository.get_all()


    # -----------------------
    # GET USER BY ID
    # -----------------------
    @staticmethod
    def get_by_id(user_id: str):
        user = UserRepository.get_by_id(user_id)

        if not user:
            logger.warning("User not found: %s", user_id)
            return None  # Let controller handle 404

        return user
    
    # -----------------------
    # GET USER BY ID
    # -----------------------
    @staticmethod
    def get_current_user(user):
        """
        Get the current logged-in user's profile.
        
        Business logic:
        - Verify user is active
        - Optional: load permissions or additional data
        - Log the access
        """
        logger.info("Fetching profile for user: %s", user.user_id)
        
        if not user.is_active:
            logger.warning("Attempted profile access by inactive user: %s", user.user_id)
            raise BadRequest("User account is inactive")
        
        logger.info("Successfully retrieved profile for user: %s", user.user_id)
        return user

    # -----------------------
    # UPDATE USER
    # -----------------------
    @staticmethod
    def update(user, data: dict):
        logger.info("Updating user: %s", user.user_id)

        # Handle password update safely
        if "password" in data and data["password"]:
            data["password"] = hash_password(data["password"])

        for key, value in data.items():
            setattr(user, key, value)

        return UserRepository.update(user)


    # -----------------------
    # DELETE USER
    # -----------------------
    @staticmethod
    def delete(user):
        logger.info("Deleting user: %s", user.user_id)
        UserRepository.delete(user)
        return True