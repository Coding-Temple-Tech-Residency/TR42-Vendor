from models import Contractor, db

class ContractorRepository:

    @staticmethod
    def get_all():
        return Contractor.query.all()

    @staticmethod
    def get_by_id(contractor_id):
        return Contractor.query.get(contractor_id)

    @staticmethod
    def create(contractor):
        db.session.add(contractor)
        db.session.commit()
        return contractor

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(contractor):
        db.session.delete(contractor)
        db.session.commit()