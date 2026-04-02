from app.extensions import db
from .model import VendorUser
from uuid import uuid4


class VendorUserRepository:

    @staticmethod
    def assign_user(data):
        link = VendorUser(
            id=str(uuid4()),
            user_id=data["user_id"],
            vendor_id=data["vendor_id"],
            role=data["role"],
            created_by="system",   
            updated_by="system"    
        )

        db.session.add(link)
        db.session.commit()

        # Reload with relationships
        link = VendorUser.query.get(link.id)

        return link

    @staticmethod
    def get_users_for_vendor(vendor_id: str):
        return VendorUser.query.filter_by(vendor_id=vendor_id).all()

    @staticmethod
    def get_vendors_for_user(user_id: str):
        return VendorUser.query.filter_by(user_id=user_id).all()

    @staticmethod
    def delete_link(link_id: str):
        link = VendorUser.query.get(link_id)
        if not link:
            return None
        db.session.delete(link)
        db.session.commit()
        return True