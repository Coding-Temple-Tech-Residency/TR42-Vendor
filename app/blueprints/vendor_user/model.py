from app.extensions import db
from sqlalchemy.dialects.postgresql import ENUM



"""
    VendorUser database model representing the relationship between vendor and user entities.

    Attributes:
        id (str): Primary key identifier for the vendor user record.
        user_id (str): Foreign key reference to the associated user. Required.
        vendor_id (str): Foreign key reference to the associated vendor.
        role (str): User role within the vendor context. Can represent core role options.
        created_at (datetime): Timestamp when the record was created.
        updated_at (datetime): Timestamp when the record was last updated.
        created_by (str): Identifier of the user who created this record. Required.
        updated_by (str): Identifier of the user who last updated this record. Required.
    """
class VendorUser(db.Model):
   
    __tablename__ = "vendor_user"

    id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String, nullable=False)
    vendor_id = db.Column(db.String)
    role = db.Column(
        ENUM(
            'admin',
            'manager',
            'supervisor',
            name='role_options',
            schema='core',
            create_type=False
        ),
        nullable=False
    )
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    created_by = db.Column(db.String, nullable=False)
    updated_by = db.Column(db.String, nullable=False)
