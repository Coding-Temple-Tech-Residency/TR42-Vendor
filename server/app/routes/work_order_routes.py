def create_work_order_service(data):
    wo = WorkOrder(**data)
    db.session.add(wo)
    db.session.commit()
    return wo


def get_all_work_orders_service():
    return WorkOrder.query.all()


def get_work_order_service(work_order_id):
    wo = WorkOrder.query.get(work_order_id)
    if not wo:
        raise ValueError("Work order not found")
    return wo


def update_work_order_service(work_order_id, data):
    wo = get_work_order_service(work_order_id)

    for key, value in data.items():
        setattr(wo, key, value)

    db.session.commit()
    return wo


def delete_work_order_service(work_order_id):
    wo = get_work_order_service(work_order_id)
    db.session.delete(wo)
    db.session.commit()