from models import Ticket, db

class TicketRepository:

    @staticmethod
    def get_all():
        return Ticket.query.all()

    @staticmethod
    def get_by_id(ticket_id):
        return Ticket.query.get(ticket_id)

    @staticmethod
    def create(ticket):
        db.session.add(ticket)
        db.session.commit()
        return ticket

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(ticket):
        db.session.delete(ticket)
        db.session.commit()