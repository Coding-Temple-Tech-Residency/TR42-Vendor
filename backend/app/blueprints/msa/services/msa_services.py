from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest

from app.blueprints.msa.model import MSA
from app.blueprints.msa.repositories.msa_repositories import MSARepository
from app.blueprints.msa.schemas import msa_schema


class MSAService:

    @staticmethod
    def create(data: dict) -> MSA:
        try:
            # Marshmallow validates and constructs the MSA instance
            msa = msa_schema.load(data)
            return MSARepository.create(msa)
        except ValidationError as e:
            raise BadRequest(e.messages)

    @staticmethod
    def get_all():
        return MSARepository.get_all()

    @staticmethod
    def get(msa_id: str):
        return MSARepository.get(msa_id)

    @staticmethod
    def update(msa: MSA, data: dict) -> MSA:
        try:
            # Partial=True allows updating only provided fields
            updated_msa = msa_schema.load(
                data,
                instance=msa,
                partial=True
            )
            return MSARepository.update(updated_msa)
        except ValidationError as e:
            raise BadRequest(e.messages)

    @staticmethod
    def delete(msa: MSA) -> None:
        return MSARepository.delete(msa)
