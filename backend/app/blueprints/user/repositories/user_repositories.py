from sqlalchemy import select
from app.extensions import db
from app.blueprints.user.model import User
from logging import getLogger
from app.blueprints.vendor_user.model import VendorUser

logger = getLogger(__name__)


class UserRepository:

    @staticmethod
    def get_by_vendor_paginated(vendor_id: str, page: int = 1, per_page: int = 10):
        stmt = (
            select(User)
            .join(VendorUser, VendorUser.user_id == User.user_id)
            .where(VendorUser.vendor_id == vendor_id)
        )
        return db.paginate(stmt, page=page, per_page=per_page)

    @staticmethod
    def get_all_paginated(page: int = 1, per_page: int = 10):
        return db.paginate(select(User), page=page, per_page=per_page)

    @staticmethod
    def get_all():
        logger.debug("Fetching all users")
        return db.session.query(User).all()

    @staticmethod
    def get_by_id(user_id: str):
        logger.debug("Fetching user by id: %s", user_id)
        return db.session.get(User, user_id)

    @staticmethod
    def get_by_email(email: str) -> User | None:
        logger.debug("Fetching user by email: %s", email)
        return db.session.scalar(select(User).where(User.email == email))

    @staticmethod
    def get_by_username(username: str) -> User | None:
        logger.debug("Fetching user by username: %s", username)
        return db.session.scalar(select(User).where(User.username == username))

    @staticmethod
    def create(user: User) -> User:
        logger.debug(
            "Adding user to session: username=%s, email=%s",
            user.username,
            user.email,
        )
        db.session.add(user)
        return user

    @staticmethod
    def update(user: User, data: dict):
        for key, value in data.items():
            setattr(user, key, value)
            db.session.commit()
            return user

    @staticmethod
    def delete(user: User):
        db.session.delete(user)
        db.session.commit()
