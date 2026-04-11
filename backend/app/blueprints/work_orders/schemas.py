from app.extensions import ma
from app.blueprints.work_orders.model import WorkOrder


class WorkOrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WorkOrder
        load_instance = True


work_order_schema = WorkOrderSchema()
work_orders_schema = WorkOrderSchema(many=True)