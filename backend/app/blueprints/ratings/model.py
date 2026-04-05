from app.extensions import db
from app.models.base import BaseModel
from datetime import datetime

class Rating(BaseModel): #rename ContractorPerformance 
    __tablename__ = 'ratings'

    rating_id = db.Column(db.String, primary_key=True)
    rating_value = db.Column(db.Integer) #1.0 to 5.0
    comments = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    tickets_open = db.Column(db.Integer)
    on_time_rate = db.Column(db.Float) #percentage of tickets completed on time
    
    contractor_id = db.Column(db.String, db.ForeignKey('contractors.contractor_id'))
    contractor = db.relationship('Contractor', back_populates='ratings')
    tickets_completed = db.Column(db.Integer)
    created_by = db.Column(db.String, db.ForeignKey('users.user_id')) #not sure well need this... but user_id of the person who created the rating
    updatetd_by = db.Column(db.String, db.ForeignKey('users.user_id')) #not sure well need this but..user_id of the person who last updated the rating

    