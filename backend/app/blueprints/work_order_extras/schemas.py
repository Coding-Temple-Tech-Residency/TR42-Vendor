from app.extensions import ma
from app.blueprints.work_order_extras.model import CancelledWorkOrder





class CancelledWorkOrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CancelledWorkOrder
        load_instance = True
        include_fk = True



cancelled_work_order_schema = CancelledWorkOrderSchema()
cancelled_work_orders_schema = CancelledWorkOrderSchema(many=True)