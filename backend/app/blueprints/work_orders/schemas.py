from app.extensions import ma
from app.blueprints.work_orders.model import WorkOrder, OrderStatus, PriorityStatus
from marshmallow import fields, ValidationError


class EnumField(fields.Field):
    """Custom field for serializing/deserializing enum values"""
    
    def __init__(self, enum_class, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.enum_class = enum_class
    
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return value.value
    
    def _deserialize(self, value, attr, data, **kwargs):
        if value is None:
            return None
        try:
            return self.enum_class(value)
        except ValueError:
            raise ValidationError(f"Invalid value for {self.enum_class.__name__}: {value}")


class WorkOrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WorkOrder
        load_instance = True
        include_fk = True

    current_status = EnumField(OrderStatus, data_key='current_status')
    priority = EnumField(PriorityStatus, data_key='priority')


work_order_schema = WorkOrderSchema()
work_orders_schema = WorkOrderSchema(many=True)