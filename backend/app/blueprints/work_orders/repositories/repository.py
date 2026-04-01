from models import WorkOrder, db

class WorkOrderRepository:
    
    @staticmethod
    def get_all():
        return WorkOrder.query.all()
    
    @staticmethod
    def get_by_id(work_order_id):
        return WorkOrder.query.get(work_order_id)
    
    @staticmethod
    def create(work_order):
        db.session.add(work_order)
        db.session.commit()
        return work_order
    
    @staticmethod
    def update():
        db.session.commit()
    
    @staticmethod
    def delete(work_order):
        db.session.delete(work_order)
        db.session.commit()