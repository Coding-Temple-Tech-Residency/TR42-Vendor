@contractor_bp.route("/contractors", methods=["GET"])
def get_contractors():
    return ContractorSchema(many=True).dump(get_all_contractors_service())


@contractor_bp.route("/contractors/<int:id>", methods=["GET"])
def get_contractor(id):
    return ContractorSchema().dump(get_contractor_service(id))