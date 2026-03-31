# def assign_ticket_service(ticket_id, contractor_id):
#     ticket = Ticket.query.get(ticket_id)
    
#     if not ticket:
#         raise ValueError("Ticket not found")
    
#     contractor = Contractor.query.get(contractor_id)
    
#     if not contractor:
#         raise ValueError("Contractor not found")
    
#     if contractor.contractor_status != "active":
#         raise ValueError("Contractor is not active")
    
#     ticket.assigned_contractor_id = contractor_id
    
#     db.session.commit()
    
#     return ticket