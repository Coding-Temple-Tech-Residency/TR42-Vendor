from app.extensions import db
from app.blueprints.msa_requirements.model import MSARequirements


class MSARequirementsRepository:

    @staticmethod
    def create(req: MSARequirements) -> MSARequirements:
        db.session.add(req)
        db.session.commit()
        return req

    @staticmethod
    def get(req_id: str) -> MSARequirements | None:
        return MSARequirements.query.get(req_id)

    @staticmethod
    def get_by_msa(msa_id: str) -> list[MSARequirements]:
        return MSARequirements.query.filter_by(msa_id=msa_id).all()

    @staticmethod
    def update(req: MSARequirements) -> MSARequirements:
        db.session.commit()
        return req

    @staticmethod
    def delete(req: MSARequirements) -> None:
        db.session.delete(req)
        db.session.commit()
