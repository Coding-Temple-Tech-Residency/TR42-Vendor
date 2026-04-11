from app.extensions import db
from sqlalchemy.sql import func



class License(db.Model):
    __tablename__ = 'licenses'

    license_id = db.Column(db.String, primary_key=True)

    contractor_id = db.Column(
        db.String,
        db.ForeignKey('contractors.contractor_id'),
        nullable=False
    )

    license_type = db.Column(db.String(100), nullable=False)
    license_number = db.Column(db.String(100), nullable=False)
    license_state = db.Column(db.String(2), nullable=False)

    license_expiration_date = db.Column(db.DateTime, nullable=False)

    license_document_url = db.Column(db.String(100))

    license_verified = db.Column(db.Boolean, default=False)

    license_verified_by = db.Column(
        db.String,
        db.ForeignKey('vendor.vendor_id')  # verifier is a vendor
    )

    license_verified_at = db.Column(db.DateTime)

    # audit fields
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())

    created_by = db.Column(
        db.String,
        db.ForeignKey('user.user_id'),
        nullable=False
    )

    updated_by = db.Column(
        db.String,
        db.ForeignKey('user.user_id')
    )

    # ----------------------
    # 🔗 Relationships
    # ----------------------

    contractor = db.relationship('Contractor', foreign_keys=[contractor_id], backref='licenses')

    verifier = db.relationship('Vendor', backref='verified_licenses')

    creator = db.relationship('User', foreign_keys=[created_by])
    updater = db.relationship('User', foreign_keys=[updated_by])