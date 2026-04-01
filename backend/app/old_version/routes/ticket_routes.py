@ticket_bp.route("/tickets", methods=["POST"])
def create_ticket():
    data = request.get_json()
    ticket = create_ticket_service(data)
    return TicketSchema().dump(ticket), 201


@ticket_bp.route("/tickets", methods=["GET"])
def get_all_tickets():
    tickets = get_all_tickets_service()
    return TicketSchema(many=True).dump(tickets), 200


@ticket_bp.route("/tickets/<int:id>", methods=["GET"])
def get_ticket(id):
    ticket = get_ticket_by_id_service(id)
    return TicketSchema().dump(ticket), 200


@ticket_bp.route("/tickets/<int:id>", methods=["PUT"])
def update_ticket(id):
    data = request.get_json()
    ticket = update_ticket_service(id, data)
    return TicketSchema().dump(ticket), 200


@ticket_bp.route("/tickets/<int:id>", methods=["DELETE"])
def delete_ticket(id):
    delete_ticket_service(id)
    return {"message": "deleted"}, 200


@ticket_bp.route("/tickets/<int:id>/assign", methods=["POST"])
def assign_ticket(id):
    contractor_id = request.json.get("contractor_id")
    ticket = assign_ticket_service(id, contractor_id)
    return TicketSchema().dump(ticket), 200