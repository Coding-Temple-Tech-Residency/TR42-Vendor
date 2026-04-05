from sqlalchemy import select
from app.extensions import db
from app.blueprints.user.model import User
from logging import getLogger

logger = getLogger(__name__)


class UserRepository:

    # @staticmethod
    # def get_all():
    #     return db.session.query(User).all()

    # @staticmethod
    # def get_by_id(user_id: str):
    #     return db.session.get(User, user_id)

    @staticmethod
    def get_by_email(email: str) -> User | None:
        return db.session.scalar(select(User).where(User.email == email))

    @staticmethod
    def get_by_username(username: str) -> User | None:
        return db.session.scalar(select(User).where(User.username == username))

    @staticmethod
    def create(user: User) -> User:
        db.session.add(user)
        return user

    # @staticmethod
    # def update(user: User, data: dict):
    #     for key, value in data.items():
    #         setattr(user, key, value)
    #     db.session.commit()
    #     return user

    # @staticmethod
    # def delete(user: User):
    #     db.session.delete(user)
    #     db.session.commit()
