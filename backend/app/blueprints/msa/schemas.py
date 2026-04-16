from app.extensions import ma
from app.blueprints.msa.model import MSA


class MSASchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MSA
        load_instance = True
        include_fk = True
        


msa_schema = MSASchema()
msas_schema = MSASchema(many=True)
