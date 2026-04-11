from app.blueprints.ticket.repositories.repository import TicketRepository
from app.blueprints.ticket.model import Ticket

class TicketService:

    @staticmethod
    def get_all_tickets():
        return TicketRepository.get_all()

    @staticmethod
    def get_ticket(ticket_id):
        return TicketRepository.get_by_id(ticket_id)

    @staticmethod
    def create_ticket(data):
        ticket = Ticket(**data)
        return TicketRepository.create(ticket)

    @staticmethod
    def update_ticket(ticket, data):
        for key, value in data.items():
            setattr(ticket, key, value)
        TicketRepository.update()
        return ticket

    @staticmethod
    def delete_ticket(ticket):
        TicketRepository.delete(ticket)
        return True