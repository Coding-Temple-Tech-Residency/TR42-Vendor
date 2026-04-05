from app.extensions import db
from app.blueprints.user.model import User
from app.blueprints.user.repositories.user_repository import UserRepository


def test_add_user(app):
    with app.app_context():
        user = User(
            username="jane123",
            email="jane@example.com",
            first_name="Jane",
            last_name="Doe",
            user_type="vendor",
            is_active=True,
            is_admin=False,
            password_hash="hashed-password",
        )

        saved_user = UserRepository.create(user)

        assert saved_user.user_id is not None
        assert saved_user.username == "jane123"


def test_get_by_email(app):
    with app.app_context():
        user = User(
            username="john123",
            email="john@example.com",
            first_name="John",
            last_name="Doe",
            user_type="vendor",
            is_active=True,
            is_admin=False,
            password_hash="hashed-password",
        )
        db.session.add(user)
        db.session.commit()

        found_user = UserRepository.get_by_email("john@example.com")

        assert found_user is not None
        assert found_user.email == "john@example.com"


def test_get_by_username(app):
    with app.app_context():
        user = User(
            username="mary123",
            email="mary@example.com",
            first_name="Mary",
            last_name="Doe",
            user_type="vendor",
            is_active=True,
            is_admin=False,
            password_hash="hashed-password",
        )
        db.session.add(user)
        db.session.commit()

        found_user = UserRepository.get_by_username("mary123")

        assert found_user is not None
        assert found_user.username == "mary123"
