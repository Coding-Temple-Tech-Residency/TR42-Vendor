from app.blueprints.vendor_users.vendor_users_repository import VendorUserRepository


class VendorUserService:

    @staticmethod
    def assign_user(data):
        return VendorUserRepository.assign_user(data)

    @staticmethod
    def get_users_for_vendor(vendor_id):
        return VendorUserRepository.get_users_for_vendor(vendor_id)

    @staticmethod
    def get_vendors_for_user(user_id):
        return VendorUserRepository.get_vendors_for_user(user_id)

    @staticmethod
    def delete_link(link_id):
        return VendorUserRepository.delete_link(link_id)