from app.extensions import db
from sqlalchemy import func


class Certification(db.Model):
    __tablename__ = 'certifications'

    certification_id = db.Column(db.String, primary_key=True)

    contractor_id = db.Column(
        db.String,
        db.ForeignKey('contractors.contractor_id'),
        nullable=False
    )

    certification_name = db.Column(db.String)
    certifying_body = db.Column(db.String)

    certification_number = db.Column(db.Integer, nullable=False)

    issue_date = db.Column(db.DateTime, nullable=False)
    expiration_date = db.Column(db.DateTime)

    certification_document_url = db.Column(db.String(100))

    certification_verified = db.Column(db.Boolean, default=False)

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

    contractor = db.relationship('Contractor', backref='certifications')

    creator = db.relationship('User', foreign_keys=[created_by])
    updater = db.relationship('User', foreign_keys=[updated_by])