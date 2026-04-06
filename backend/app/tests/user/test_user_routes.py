import pytest
from unittest.mock import patch


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
        self.created_by_user_id = None
        self.updated_by_user_id = None
        self.profile_photo = None


def test_create_user_success(client):
    payload = {
        "username": "jane123",
        "password": "secret1",
        "email": "jane@example.com",
        "first_name": "Jane",
        "last_name": "Doe",
        "user_type": "VENDOR",
        "is_active": True,
        "is_admin": False,
    }

    mock_user = MockUser()

    with patch(
        "app.blueprints.user.controller.user_routes.user_schema.load",
        return_value=payload,
    ), patch(
        "app.blueprints.user.controller.user_routes.UserService.create_user",
        return_value=mock_user,
    ), patch(
        "app.blueprints.user.controller.user_routes.user_schema.dump",
        return_value={
            "username": "jane123",
            "email": "jane@example.com",
            "first_name": "Jane",
            "last_name": "Doe",
            "user_type": "VENDOR",
            "is_active": True,
            "is_admin": False,
        },
    ):
        response = client.post("/users/", json=payload)

    assert response.status_code == 201
    data = response.get_json()
    assert data["username"] == "jane123"
    assert data["email"] == "jane@example.com"
    assert "password" not in data
    assert "password_hash" not in data
