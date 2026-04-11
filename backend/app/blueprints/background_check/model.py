from app.extensions import db
from datetime import datetime

class BackgroundCheck(db.Model): 
    __tablename__ = 'background_check'

    background_check_id = db.Column(db.String, primary_key=True)
    
    background_check_passed = db.Column(db.Boolean)
    
    background_check_date = db.Column(db.DateTime)
    
    background_check_provider = db.Column(db.String)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    created_by_user = db.Column(db.String, db.ForeignKey('user.user_id')) 
    
    updated_by_user = db.Column(db.String, db.ForeignKey('user.user_id'))
    
    contractor_id = db.Column(db.String, db.ForeignKey('contractors.contractor_id'), nullable=False)