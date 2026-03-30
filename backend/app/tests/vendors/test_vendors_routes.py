import pytest
from unittest.mock import patch
from flask import Flask


@pytest.fixture(scope="session")
def app():
    from app.blueprints.vendors.controller.routes import vendors_bp

    app = Flask(__name__)
    app.config["TESTING"] = True
    app.register_blueprint(vendors_bp)

    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_get_vendors_success(client):
    mock_vendors = [
        {"vendor_id": "1", "company_name": "Vendor1"},
        {"vendor_id": "2", "company_name": "Vendor2"},
    ]

    with patch(
        "app.blueprints.vendors.controller.routes.VendorService.get_all_vendors",
        return_value=mock_vendors,
    ):
        response = client.get("/vendors/")
        assert response.status_code == 200
        assert response.get_json() == mock_vendors


def test_get_vendors_exception(client):
    with patch(
        "app.blueprints.vendors.controller.routes.VendorService.get_all_vendors",
        side_effect=Exception("DB error"),
    ):
        response = client.get("/vendors/")
        assert response.status_code == 500
        assert response.get_json() == {
            "error": "An error occurred while fetching vendors"
        }
