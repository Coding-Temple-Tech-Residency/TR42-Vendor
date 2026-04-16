from app.extensions import db
from app.blueprints.msa.model import MSA


class MSARepository:

    @staticmethod
    def create(msa: MSA) -> MSA:
        db.session.add(msa)
        db.session.commit()
        return msa

    @staticmethod
    def get(msa_id: str) -> MSA | None:
        return MSA.query.get(msa_id)

    @staticmethod
    def get_all() -> list[MSA]:
        return MSA.query.order_by(MSA.created_at.desc()).all()

    @staticmethod
    def update(msa: MSA) -> MSA:
        db.session.commit()
        return msa

    @staticmethod
    def delete(msa: MSA) -> None:
        db.session.delete(msa)
        db.session.commit()
