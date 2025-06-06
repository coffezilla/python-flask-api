# controllers/user_controller.py
from flask import jsonify, request
from ..services.users_service import get_users_service, get_user_by_id_service, post_user_service, delete_user_service, patch_user_service


def get_users():
    users = get_users_service()
    return jsonify(users), 200


def get_user_by_id(user_id):
    user = get_user_by_id_service(user_id)
    return jsonify(user), 200


def post_user():
    new_user = post_user_service()
    return jsonify(new_user), 201


def delete_user(user_id):
    user = delete_user_service(user_id)
    return jsonify(user), 200


def patch_user(user_id):
    updated_user = patch_user_service(user_id)
    return jsonify(updated_user), 200
