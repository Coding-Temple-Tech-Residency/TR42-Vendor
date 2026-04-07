from unittest.mock import patch

import pytest

from app.blueprints.user.services.user_services import UserService


class MockUser:
    def __init__(self):
        self.user_id = "123"
        self.username = "jane123"
        self.email = "jane@example.com"
        self.first_name = "Jane"
        self.last_name = "Doe"
        self.user_type = "VENDOR"
        self.is_active = True
        self.is_admin = False
        self.token_version = 0
        self.password_hash = ""

    def set_password(self, raw_password: str) -> None:
        self.password_hash = f"hashed::{raw_password}"

    def check_password(self, raw_password: str) -> bool:
        return self.password_hash == f"hashed::{raw_password}"


def test_create_user_success():
    data = {
        "username": "jane123",
        "password": "secret1",
        "email": "jane@example.com",
        "first_name": "Jane",
        "last_name": "Doe",
        "user_type": "VENDOR",
        "is_active": True,
        "is_admin": False,
    }

    with patch(
        "app.blueprints.user.services.user_services.UserRepository.get_by_email",
        return_value=None,
    ), patch(
        "app.blueprints.user.services.user_services.UserRepository.get_by_username",
        return_value=None,
    ), patch(
        "app.blueprints.user.services.user_services.UserRepository.create"
    ) as mock_create, patch(
        "app.blueprints.user.services.user_services.db.session.commit"
    ):
        created_user = UserService.create_user(data.copy())

    assert created_user.username == "jane123"
    assert created_user.email == "jane@example.com"
    assert created_user.first_name == "Jane"
    assert created_user.last_name == "Doe"
    mock_create.assert_called_once()


def test_create_user_duplicate_email():
    data = {
        "username": "jane123",
        "password": "secret1",
        "email": "jane@example.com",
        "first_name": "Jane",
        "last_name": "Doe",
        "user_type": "VENDOR",
        "is_active": True,
        "is_admin": False,
    }

    existing_user = MockUser()

    with patch(
        "app.blueprints.user.services.user_services.UserRepository.get_by_email",
        return_value=existing_user,
    ):
        with pytest.raises(ValueError, match="Email already exists"):
            UserService.create_user(data.copy())


def test_create_user_duplicate_username():
    data = {
        "username": "jane123",
        "password": "secret1",
        "email": "jane@example.com",
        "first_name": "Jane",
        "last_name": "Doe",
        "user_type": "VENDOR",
        "is_active": True,
        "is_admin": False,
    }

    with patch(
        "app.blueprints.user.services.user_services.UserRepository.get_by_email",
        return_value=None,
    ), patch(
        "app.blueprints.user.services.user_services.UserRepository.get_by_username",
        return_value=MockUser(),
    ):
        with pytest.raises(ValueError, match="Username already exists"):
            UserService.create_user(data.copy())
