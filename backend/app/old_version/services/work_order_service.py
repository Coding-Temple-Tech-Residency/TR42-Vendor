@work_order_bp.route("/work-orders", methods=["POST"])
def create_work_order():
    data = request.get_json()
    wo = create_work_order_service(data)
    return WorkOrderSchema().dump(wo), 201


@work_order_bp.route("/work-orders", methods=["GET"])
def get_work_orders():
    return WorkOrderSchema(many=True).dump(get_all_work_orders_service())


@work_order_bp.route("/work-orders/<id>", methods=["GET"])
def get_work_order(id):
    return WorkOrderSchema().dump(get_work_order_service(id))


@work_order_bp.route("/work-orders/<id>", methods=["PUT"])
def update_work_order(id):
    data = request.get_json()
    return WorkOrderSchema().dump(update_work_order_service(id, data))


@work_order_bp.route("/work-orders/<id>", methods=["DELETE"])
def delete_work_order(id):
    delete_work_order_service(id)
    return {"message": "deleted"}