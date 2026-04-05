from flask import Blueprint, request
from ..services.user_service import UserService
from ..schemas import user_schema, users_schema
from flask import Blueprint, request


user_bp = Blueprint("user_bp", __name__)


@user_bp.post("/login")
def login_user():
    data = request.get_json()
    result = UserService.login(data)
    return result, 200



@user_bp.post("/")
def create_user():
    data = request.get_json()
    user = UserService.create(data)
    return user_schema.dump(user), 201

# @user_bp.get("/")
# def get_users():
#     users = UserService.get_all()
#     return users_schema.dump(users), 200

