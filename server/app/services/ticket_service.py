def create_ticket_service(data):
    ticket = Ticket(**data)
    db.session.add(ticket)
    db.session.commit()
    return ticket


def get_all_tickets_service():
    return Ticket.query.all()


def get_ticket_by_id_service(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    if not ticket:
        raise ValueError("Ticket not found")
    return ticket


def update_ticket_service(ticket_id, data):
    ticket = get_ticket_by_id_service(ticket_id)

    for key, value in data.items():
        setattr(ticket, key, value)

    db.session.commit()
    return ticket


def delete_ticket_service(ticket_id):
    ticket = get_ticket_by_id_service(ticket_id)
    db.session.delete(ticket)
    db.session.commit()