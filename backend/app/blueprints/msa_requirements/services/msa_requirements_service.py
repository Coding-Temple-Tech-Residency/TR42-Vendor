from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest

from app.blueprints.msa_requirements.model import MSARequirements
from app.blueprints.msa_requirements.repositories.msa_requirements_repositories import MSARequirementsRepository
from app.blueprints.msa_requirements.schemas import msa_req_schema


class MSARequirementsService:

    @staticmethod
    def create(msa_id: str, data: dict) -> MSARequirements:
        try:
            # Inject msa_id into the payload before validation
            data["msa_id"] = msa_id

            # Marshmallow validates and constructs the instance
            req = msa_req_schema.load(data)
            return MSARequirementsRepository.create(req)

        except ValidationError as e:
            raise BadRequest(e.messages)

    @staticmethod
    def update(req: MSARequirements, data: dict) -> MSARequirements:
        try:
            # Partial=True allows updating only provided fields
            updated_req = msa_req_schema.load(
                data,
                instance=req,
                partial=True
            )
            return MSARequirementsRepository.update(updated_req)

        except ValidationError as e:
            raise BadRequest(e.messages)

    @staticmethod
    def delete(req: MSARequirements) -> None:
        return MSARequirementsRepository.delete(req)
