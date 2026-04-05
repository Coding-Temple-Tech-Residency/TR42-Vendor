import pytest
from unittest.mock import patch

from app import create_app


class MockUser:
    def __init__(self):
        self.user_id = "123"
        self.username = "jane123"
        self.email = "jane@example.com"
        self.first_name = "Jane"
        self.last_name = "Doe"
        self.user_type = "vendor"
        self.is_active = True
        self.is_admin = False
        self.token_version = 0
        self.created_by_user_id = None
        self.updated_by_user_id = None
        self.profile_photo = None


@pytest.fixture(scope="session")
def app():
    app = create_app()
    app.config["TESTING"] = True
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_create_user_success(client):
    payload = {
        "username": "jane123",
        "password": "secret1",
        "email": "jane@example.com",
        "first_name": "Jane",
        "last_name": "Doe",
        "user_type": "vendor",
        "is_active": True,
        "is_admin": False,
    }

    mock_user = MockUser()

    with patch(
        "app.blueprints.user.controller.routes.UserService.create_user",
        return_value=mock_user,
    ):
        response = client.post("/users/", json=payload)

    assert response.status_code == 201
    data = response.get_json()
    assert data["username"] == "jane123"
    assert data["email"] == "jane@example.com"
    assert "password" not in data
    assert "password_hash" not in data


def test_create_user_no_data(client):
    response = client.post("/users/", json=None)

    assert response.status_code == 400
    assert response.get_json() == {"error": "No input data provided"}


def test_create_user_service_exception(client):
    payload = {
        "username": "jane123",
        "password": "secret1",
        "email": "jane@example.com",
        "first_name": "Jane",
        "last_name": "Doe",
        "user_type": "vendor",
        "is_active": True,
        "is_admin": False,
    }

    with patch(
        "app.blueprints.user.controller.routes.UserService.create_user",
        side_effect=Exception("DB error"),
    ):
        response = client.post("/users/", json=payload)

    assert response.status_code == 500
