from app.extensions import db
from app.models.base import BaseModel

class TicketPhoto(BaseModel):
    __tablename__ = 'ticket_photos'

    photo_id = db.Column(db.String, primary_key=True)

    ticket_id = db.Column(db.String, db.ForeignKey('ticket.ticket_id'))
    uploaded_by = db.Column(db.String, db.ForeignKey('contractors.contractor_id'))

    photo_content = db.Column(db.LargeBinary)

    ticket = db.relationship('Ticket', backref='photos')