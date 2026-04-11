from app.extensions import db
from datetime import datetime

class ContractorPerformance(db.Model): 
    __tablename__ = 'contractor_performance'

    rating_id = db.Column(db.String, primary_key=True)
    rating = db.Column(db.Integer) #1.0 to 5.0
    comments = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    ticket_id = db.Column(db.String, db.ForeignKey('ticket.ticket_id'))
    contractor_id = db.Column(db.String, db.ForeignKey('contractors.contractor_id'))
    created_by_user = db.Column(db.String, db.ForeignKey('user.user_id')) 
    updated_by_user = db.Column(db.String, db.ForeignKey('user.user_id')) 

