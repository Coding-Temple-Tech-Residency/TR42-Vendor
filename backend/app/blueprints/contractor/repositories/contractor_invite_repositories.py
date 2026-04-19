from datetime import datetime
from app.blueprints.contractor.ContractorInviteModel import ContractorInvite


class ContractorInviteRepository:

    @staticmethod
    def get_valid_by_token(token: str):
        invite = ContractorInvite.query.filter_by(token=token).first()

        if not invite:
            return None

        if invite.is_used:
            return None

        if invite.expires_at < datetime.utcnow():
            return None

        return invite
