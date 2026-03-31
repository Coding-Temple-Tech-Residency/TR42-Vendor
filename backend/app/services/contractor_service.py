def get_all_contractors_service():
    return Contractor.query.all()


def get_contractor_service(contractor_id):
    contractor = Contractor.query.get(contractor_id)
    if not contractor:
        raise ValueError("Contractor not found")
    return contractor