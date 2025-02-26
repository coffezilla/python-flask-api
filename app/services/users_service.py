from flask import jsonify, request
import uuid
from ..models.user import User
from ..utils.uuid import is_valid_uuid
from ..models import db


# get


def get_users_service():
    users = User.query.all()
    return [user.to_dict() for user in users]


# get by id


def get_user_by_id_service(user_id):
    if not is_valid_uuid(user_id):
        return {"message": "UUID não válido"}

    user = User.query.get(user_id)

    if user is None:
        return {"error": "User not found"}

    return user.to_dict()


# post
def post_user_service():
    data = request.get_json()

    if not data or 'username' not in data or 'email' not in data:
        return {"message": "Missing some attribute"}

    new_user = User(
        id=str(uuid.uuid4()),  # Use UUID for user ID
        username=data['username'],
        email=data['email'],
    )

    db.session.add(new_user)
    db.session.commit()

    return new_user.to_dict()


# patch
def patch_user_service(user_id):

    if not is_valid_uuid(user_id):
        return {"message": "UUID não válido"}

    user = User.query.get(user_id)

    if user is None:
        return {"message": "User not found"}

    data = request.get_json()

    # Only update fields that are provided
    if 'username' in data:
        user.username = data['username']
    if 'email' in data:
        user.email = data['email']

    db.session.commit()

    return user.to_dict()


# delete
def delete_user_service(user_id):
    if not is_valid_uuid(user_id):
        return {"message": "UUID não válido"}

    user = User.query.get(user_id)

    if user is None:
        return {"message": "User not found"}

    db.session.delete(user)
    db.session.commit()

    return {"message": "User deleted"}
