from app.extensions import db

class Vendor(db.Model):
    __tablename__ = "vendor"

    vendor_id = db.Column(db.String, primary_key=True)

    company_name = db.Column(db.String(80), nullable=False, unique=True)
    company_code = db.Column(db.String)

    primary_contact_name = db.Column(db.String, nullable=False)
    company_email = db.Column(db.String, nullable=False)
    company_phone = db.Column(db.String, nullable=False)

    status = db.Column(
        db.Enum("active", "inactive", name="vendor_status"),
        nullable=False
    )

    onboarding = db.Column(db.Boolean, nullable=False)

    compliance_status = db.Column(
        db.Enum("expired", "incomplete", "complete", name="compliance_status")
    )

    #description = db.Column(db.Text)

    address_id = db.Column(db.String, db.ForeignKey("address.address_id"))
    created_by = db.Column(db.String, default="system")
    updated_by = db.Column(db.String, default="system")

    # FIXED: use back_populates instead of backref
    address = db.relationship("Address", back_populates="vendor")

    users = db.relationship("VendorUser", back_populates="vendor")
    
