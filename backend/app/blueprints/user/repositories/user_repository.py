from app.extensions import db
from ..model import User
import uuid
from uuid import uuid4
from logging import getLogger

logger = getLogger(__name__)
class UserRepository:

    @staticmethod
    def get_by_username(username: str):
        logger.info("Querying user by username: %s", username)
        return User.query.filter_by(username=username).first()


    # @staticmethod
    # def get_all():
    #     return db.session.query(User).all()

    # @staticmethod
    # def get_by_id(user_id: str):
    #     return db.session.get(User, user_id)

    @staticmethod
    def create(data: dict):
        user = User(
            user_id=str(uuid.uuid4()),  
            username=data["username"],
            password=data["password"],
            email=data["email"],
            type=data.get("type", "user"),
            is_active=data.get("is_active", True),
            is_admin=data.get("is_admin", False),
            profile_photo=data.get("profile_photo"),
            created_by=data.get("created_by", "system"),
            updated_by=data.get("updated_by", "system"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name")
        )
        db.session.add(user)
        db.session.commit()
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