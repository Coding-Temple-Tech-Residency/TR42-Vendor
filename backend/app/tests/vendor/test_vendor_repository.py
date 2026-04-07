import pytest

from app import create_app
from app.extensions import db
from app.blueprints.vendor.model import Vendor
from app.blueprints.vendor.repositories.vendor_repositories import VendorRepository
import uuid


def test_get_all_returns_all_vendors(clean_db):
    vendor1 = Vendor()
    vendor1.company_name = "Vendor One"
    vendor1.primary_contact_name = "Jane Doe"
    vendor1.company_email = "one@test.com"
    vendor1.company_phone = "111-111-1111"
    vendor1.address_id = str(uuid.uuid4())

    vendor2 = Vendor()
    vendor2.company_name = "Vendor Two"
    vendor2.primary_contact_name = "John Doe"
    vendor2.company_email = "two@test.com"
    vendor2.company_phone = "222-222-2222"
    vendor2.address_id = str(uuid.uuid4())

    db.session.add_all([vendor1, vendor2])
    db.session.commit()

    result = VendorRepository.get_all()

    assert len(result) == 2


def test_get_by_company_name_returns_vendor(clean_db):
    vendor = Vendor()
    vendor.company_name = "Test Vendor"
    vendor.primary_contact_name = "Jane Doe"
    vendor.company_email = "test@test.com"
    vendor.company_phone = "123-456-7890"
    vendor.address_id = str(uuid.uuid4())

    db.session.add(vendor)
    db.session.commit()

    result = VendorRepository.get_by_company_name("Test Vendor")

    assert result is not None
    assert result.company_name == "Test Vendor"


def test_create_saves_vendor(clean_db):
    vendor = Vendor()
    vendor.company_name = "Created Vendor"
    vendor.primary_contact_name = "Jane Doe"
    vendor.company_email = "created@test.com"
    vendor.company_phone = "999-999-9999"
    vendor.address_id = str(uuid.uuid4())

    result = VendorRepository.create(vendor)
    db.session.commit()

    assert result is not None
    assert result.vendor_id is not None
