import pytest
from unittest.mock import patch, MagicMock

from app.blueprints.vendor.model import Vendor
from app.blueprints.vendor.services.vendor_services import VendorService


@patch("app.blueprints.vendor.services.vendor_services.db.session.commit")
@patch("app.blueprints.vendor.services.vendor_services.db.session.rollback")
@patch("app.blueprints.vendor.services.vendor_services.VendorRepository")
def test_create_vendor_success(mock_repository, mock_rollback, mock_commit):
    mock_repository.get_by_company_name.return_value = None
    mock_repository.create.return_value = MagicMock()

    vendor = Vendor()
    vendor.company_name = "Test Vendor"
    vendor.primary_contact_name = "Jane Doe"
    vendor.company_email = "test@test.com"
    vendor.company_phone = "123-456-7890"

    result = VendorService.create_vendor(vendor)

    assert result is not None
    mock_repository.create.assert_called_once_with(vendor)
    mock_commit.assert_called_once()
    mock_rollback.assert_not_called()


@patch("app.blueprints.vendor.services.vendor_services.db.session.commit")
@patch("app.blueprints.vendor.services.vendor_services.db.session.rollback")
@patch("app.blueprints.vendor.services.vendor_services.VendorRepository")
def test_create_vendor_duplicate_company_name(
    mock_repository, mock_rollback, mock_commit
):
    mock_repository.get_by_company_name.return_value = MagicMock()

    vendor = Vendor()
    vendor.company_name = "Test Vendor"
    vendor.primary_contact_name = "Jane Doe"
    vendor.company_email = "test@test.com"
    vendor.company_phone = "123-456-7890"

    with pytest.raises(
        ValueError, match="Vendor with this company name already exists"
    ):
        VendorService.create_vendor(vendor)

    mock_commit.assert_not_called()
    mock_rollback.assert_called_once()
