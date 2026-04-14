from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest
from app.extensions import db

from app.blueprints.user.model import User
from app.blueprints.user.repositories.user_repositories import UserRepository
from app.blueprints.user.schemas import users_schema

from app.auth.passwords import hash_password, verify_password
from app.auth.tokens import encode_token
from app.blueprints.vendor_user.repositories.vendor_user_repositories import (
    VendorUserRepository,
)

from logging import getLogger


logger = getLogger(__name__)


class UserService:

    @staticmethod
    def login(data: dict):
        logger.info("Attempting login for user: %s", data.get("email"))

        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            logger.warning("Login failed: Missing username or password")
            raise BadRequest("Username and password are required")

        user = UserRepository.get_by_email(email)
        if not user:
            logger.warning("Login failed: user not found: %s", email)
            raise BadRequest("Invalid email or password")

        if not verify_password(password, user.password_hash):
            logger.warning("Login failed: Incorrect password for user: %s", email)
            raise BadRequest("Invalid username or password")

        vendor_links = VendorUserRepository.get_all_by_user(user.user_id)
        active_vendor_id = vendor_links[0].vendor_id if vendor_links else None

        token = encode_token(user, active_vendor_id=active_vendor_id)
        logger.info("Login successful for user: %s", email)

        return {
            "message": "Login successful",
            "token": token,
            "active_vendor_id": active_vendor_id,
            "user_id": user.user_id,
            "username": user.username,
            "email": user.email,
            "type": user.user_type.value,
            "is_admin": user.is_admin,
        }

    @staticmethod
    def get_all():
        logger.debug("Fetching all users")
        return UserRepository.get_all()

    @staticmethod
    def get_all_paginated(page: int = 1, per_page: int = 10):
        pagination = UserRepository.get_all_paginated(page=page, per_page=per_page)

        return {
            "total": pagination.total,
            "page": pagination.page,
            "pages": pagination.pages,
            "per_page": pagination.per_page,
            "users": users_schema.dump(pagination.items),
        }

    @staticmethod
    def get_vendor_users_paginated(vendor_id: str, page: int = 1, per_page: int = 10):
        pagination = UserRepository.get_by_vendor_paginated(
            vendor_id=vendor_id, page=page, per_page=per_page
        )

        return {
            "total": pagination.total,
            "page": pagination.page,
            "pages": pagination.pages,
            "per_page": pagination.per_page,
            "users": users_schema.dump(pagination.items),
        }

    @staticmethod
    def get_by_id(user_id: str):
        user = UserRepository.get_by_id(user_id)

        if not user:
            logger.warning("User not found: %s", user_id)
            return None  # Let controller handle 404

        return user

    @staticmethod
    def create_user(data: dict) -> User:
        logger.info(
            "Creating user: username=%s, email=%s",
            data.get("username"),
            data.get("email"),
        )

        existing_email = UserRepository.get_by_email(data["email"])
        if existing_email:
            logger.warning(
                "User creation failed: Email already exists: %s", data["email"]
            )
            raise ValueError("Email already exists")

        existing_username = UserRepository.get_by_username(data["username"])
        if existing_username:
            logger.warning(
                "User creation failed: Username already exists: %s",
                data["username"],
            )
            raise ValueError("Username already exists")

        user = User(
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            username=data["username"],
            user_type=data["user_type"],
            is_active=True,
            is_admin=False,
            profile_photo=data.get("profile_photo"),
        )

        logger.debug("Setting password for user: %s", data["username"])
        user.set_password(data["password"])

        try:
            UserRepository.create(user)
            logger.debug("User added to session: %s", user.username)

            db.session.commit()
            logger.info("User created successfully: %s", user.user_id)

            return user

        except IntegrityError as e:
            db.session.rollback()
            logger.exception(
                "IntegrityError during user creation for username=%s: %s",
                data.get("username"),
                e,
            )
            raise ValueError("User creation failed due to a database constraint")

        except Exception as e:
            db.session.rollback()
            logger.exception(
                "Unexpected error during user creation for username=%s: %s",
                data.get("username"),
                e,
            )
            raise

    @staticmethod
    def update(user, data: dict):
        logger.info("Updating user: %s", user.user_id)

        # Handle password update safely
        if "password" in data and data["password"]:
            data["password"] = hash_password(data["password"])

        for key, value in data.items():
            setattr(user, key, value)

        return UserRepository.update(user)

    @staticmethod
    def delete(user):
        logger.info("Deleting user: %s", user.user_id)
        UserRepository.delete(user)
        return True
