from app.extensions import ma
from app.blueprints.msa_requirements.model import MSARequirements


class MSARequirementsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MSARequirements
        load_instance = True
        include_fk = True


msa_req_schema = MSARequirementsSchema()
msa_reqs_schema = MSARequirementsSchema(many=True)
