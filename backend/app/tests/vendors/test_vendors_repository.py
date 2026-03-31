import pytest

from app import create_app
from app.extensions import db
from app.blueprints.vendors.model import Vendor
from app.blueprints.vendors.repositories.vendors_repository import VendorRepository


@pytest.fixture
def app():
    app = create_app()
    app.config["TESTING"] = True
    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def app_context(app):
    with app.app_context():
        yield


@pytest.fixture
def clean_db(app_context):
    db.drop_all()
    db.create_all()
    yield
    db.session.remove()
    db.drop_all()


def test_get_all_returns_all_vendors(clean_db):
    vendor1 = Vendor()
    vendor1.company_name = "Vendor One"
    vendor1.company_email = "one@test.com"
    vendor1.company_phone = "111-111-1111"

    vendor2 = Vendor()
    vendor2.company_name = "Vendor Two"
    vendor2.company_email = "two@test.com"
    vendor2.company_phone = "222-222-2222"

    db.session.add(vendor1)
    db.session.add(vendor2)
    db.session.commit()

    result = VendorRepository.get_all()

    assert len(result) == 2
    assert result[0].company_name == "Vendor One"
    assert result[1].company_name == "Vendor Two"


def test_get_all_returns_empty_list_when_no_vendors(clean_db):
    result = VendorRepository.get_all()

    assert result == []


def test_get_by_company_name_returns_vendor(clean_db):
    vendor = Vendor()
    vendor.company_name = "Test Vendor"
    vendor.company_email = "test@test.com"
    vendor.company_phone = "123-456-7890"

    db.session.add(vendor)
    db.session.commit()

    result = VendorRepository.get_by_company_name("Test Vendor")

    assert result is not None
    assert result.company_name == "Test Vendor"
    assert result.company_email == "test@test.com"


def test_get_by_company_name_returns_none_when_not_found(clean_db):
    result = VendorRepository.get_by_company_name("Does Not Exist")

    assert result is None


def test_create_saves_vendor(clean_db):
    vendor = Vendor()
    vendor.company_name = "Created Vendor"
    vendor.company_email = "created@test.com"
    vendor.company_phone = "999-999-9999"

    result = VendorRepository.create(vendor)

    assert result is not None
    assert result.vendor_id is not None
    assert result.company_name == "Created Vendor"

    saved_vendor = Vendor.query.filter_by(company_name="Created Vendor").first()
    assert saved_vendor is not None
    assert saved_vendor.company_email == "created@test.com"
