import pytest
from unittest.mock import patch, MagicMock
from flask import Flask, jsonify
from app.blueprints.vendor_users.controller.routes import vendor_users_bp


@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(vendor_users_bp, url_prefix="/vendor_user")
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_get_vendor_users_success(client):
    mock_users = [{"id": 1, "name": "User1"}, {"id": 2, "name": "User2"}]
    with patch(
        "app.blueprints.vendor_users.controller.routes.VendorUserService.get_all_users",
        return_value=mock_users,
    ), patch(
        "app.blueprints.vendor_users.controller.routes.vendor_users_schema.jsonify",
        return_value=jsonify(mock_users),
    ):
        response = client.get("/vendor_user/")
        assert response.status_code == 200
        assert response.get_json() == mock_users


def test_get_vendor_users_exception(client):
    with patch(
        "app.blueprints.vendor_users.controller.routes.VendorUserService.get_all_users",
        side_effect=Exception("DB error"),
    ):
        response = client.get("/vendor_user/")
        assert response.status_code == 500
        assert response.get_json() == {
            "error": "An error occurred while fetching users"
        }


def test_create_vendor_user_success(client):
    mock_user = MagicMock()
    mock_user.id = 123
    user_data = {"name": "New User"}
    with patch(
        "app.blueprints.vendor_users.controller.routes.request.get_json",
        return_value=user_data,
    ), patch(
        "app.blueprints.vendor_users.controller.routes.VendorUserService.create_user",
        return_value=mock_user,
    ), patch(
        "app.blueprints.vendor_users.controller.routes.vendor_user_schema.jsonify",
        return_value=jsonify({"id": 123, "name": "New User"}),
    ):
        response = client.post("/vendor_user/", json=user_data)
        assert response.status_code == 201
        assert response.get_json() == {"id": 123, "name": "New User"}


def test_create_vendor_user_exception(client):
    user_data = {"name": "New User"}
    with patch(
        "app.blueprints.vendor_users.controller.routes.request.get_json",
        return_value=user_data,
    ), patch(
        "app.blueprints.vendor_users.controller.routes.VendorUserService.create_user",
        side_effect=Exception("Create error"),
    ):
        response = client.post("/vendor_users/", json=user_data)
        assert response.status_code == 500
        assert response.get_json() == {
            "error": "An error occurred while creating the user"
        }
