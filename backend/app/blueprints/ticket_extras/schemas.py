from app.extensions import ma
from app.models.ticket_extras import TicketPhoto


class TicketPhotoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TicketPhoto
        load_instance = True
        exclude = ("photo_content",)  # VERY IMPORTANT


ticket_photo_schema = TicketPhotoSchema()
ticket_photos_schema = TicketPhotoSchema(many=True)