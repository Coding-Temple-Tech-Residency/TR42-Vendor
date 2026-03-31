import pytest
from unittest.mock import patch, MagicMock

from app.blueprints.vendors.services.vendors_service import VendorService
from app.blueprints.vendors.model import Vendor


@patch("app.blueprints.vendors.services.vendors_service.VendorRepository")
def test_create_vendor_success(mock_repository):
    mock_repository.get_by_company_name.return_value = None
    mock_repository.create.return_value = MagicMock()

    vendor = Vendor()
    vendor.company_name = "Test Vendor"
    vendor.company_email = "test@test.com"
    vendor.company_phone = "123-456-7890"

    result = VendorService.create_vendor(vendor)

    assert result is not None
    mock_repository.get_by_company_name.assert_called_once_with("Test Vendor")
    mock_repository.create.assert_called_once_with(vendor)


@patch("app.blueprints.vendors.services.vendors_service.VendorRepository")
def test_create_vendor_duplicate_company_name(mock_repository):
    mock_repository.get_by_company_name.return_value = MagicMock()

    vendor = Vendor()
    vendor.company_name = "Test Vendor"
    vendor.company_email = "test@test.com"
    vendor.company_phone = "123-456-7890"

    with pytest.raises(
        ValueError, match="Vendor with this company name already exists"
    ):
        VendorService.create_vendor(vendor)

    mock_repository.get_by_company_name.assert_called_once_with("Test Vendor")
    mock_repository.create.assert_not_called()
