from app.extensions import ma
from app.blueprints.work_orders.model import (
    FrequencyType,
    LocationType,
    OrderStatus,
    PriorityStatus,
    WorkOrder,
)
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
            if isinstance(value, str):
                try:
                    return self.enum_class[value.upper()]
                except KeyError:
                    pass
            raise ValidationError(f"Invalid value for {self.enum_class.__name__}: {value}")


class WorkOrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WorkOrder
        load_instance = True
        include_fk = True
        exclude = ("created_by_user_id", "updated_by_user_id")

    current_status = EnumField(OrderStatus, data_key='current_status')
    priority = EnumField(PriorityStatus, data_key='priority')
    location_type = EnumField(LocationType, data_key='location_type', allow_none=True)
    recurrence_type = EnumField(FrequencyType, data_key='recurrence_type', allow_none=True)
    created_by = fields.String(attribute='created_by_user_id', data_key='created_by', required=True)
    updated_by = fields.String(attribute='updated_by_user_id', data_key='updated_by', required=True)


work_order_schema = WorkOrderSchema()
work_orders_schema = WorkOrderSchema(many=True)