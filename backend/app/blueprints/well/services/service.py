from app.extensions import db
from app.blueprints.well.repositories.repository import WellRepository


class WellService:

    @staticmethod
    def get_all_wells():
        return WellRepository.get_all()

    @staticmethod
    def get_well(well_id):
        return WellRepository.get_by_id(well_id)

    @staticmethod
    def create_well(data):
        db.session.add(data)
        db.session.commit()
        return data

    @staticmethod
    def update_well(well_id, data):
        well = WellRepository.get_by_id(well_id)

        if not well:
            return None

        for key, value in data.items():
            setattr(well, key, value)

        db.session.commit()
        return well

    @staticmethod
    def delete_well(well_id):
        well = WellRepository.get_by_id(well_id)

        if not well:
            return None

        db.session.delete(well)
        db.session.commit()
        return well