from app.extensions import db
from datetime import datetime

class DrugTest(db.Model): 
    __tablename__ = 'drug_test'

    drug_test_id = db.Column(db.String, primary_key=True)
    drug_test_passed = db.Column(db.Boolean)
    drug_test_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by_user = db.Column(db.String, db.ForeignKey('user.user_id')) 
    updated_by_user = db.Column(db.String, db.ForeignKey('user.user_id'))