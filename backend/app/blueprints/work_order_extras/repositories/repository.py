from app.blueprints.work_order_extras.model import CancelledWorkOrder
from app.extensions import db

class CancelledWorkOrderRepository:
    
    @staticmethod
    def get_all():
        return CancelledWorkOrder.query.all()
    
    @staticmethod
    def get_by_id(cancelled_work_order_id):
        return CancelledWorkOrder.query.get(cancelled_work_order_id)
    
    @staticmethod
    def create(cancelled_work_order):
        db.session.add(cancelled_work_order)
        db.session.commit()
        return cancelled_work_order
    
    @staticmethod
    def update(cancelled_work_order):
        db.session.commit()
        return cancelled_work_order
    
    @staticmethod
    def delete(cancelled_work_order):
        db.session.delete(cancelled_work_order)
        db.session.commit()