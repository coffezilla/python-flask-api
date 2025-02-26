from flask import Blueprint, jsonify
from ..models.user import User
from ..services.users_service import get_users_service, get_user_by_id_service, post_user_service, delete_user_service, patch_user_service

user_bp = Blueprint('user_bp', __name__)


# get


@user_bp.route('/users')
def get_users():
    users = get_users_service()
    return jsonify(users)

# get by id


@user_bp.route("/users/<user_id>", methods=['GET'])
def get_user(user_id):
    user = get_user_by_id_service(user_id)
    return jsonify(user), 200

# post


@user_bp.route("/users", methods=['POST'])
def store_user():
    new_user = post_user_service()
    return jsonify(new_user), 201


# patch


@user_bp.route('/users/<user_id>', methods=['PATCH'])
def change_user(user_id):
    user = patch_user_service(user_id)
    return jsonify(user), 200

# delete


@user_bp.route("/users/<user_id>", methods=['DELETE'])
def delete_user(user_id):
    user = delete_user_service(user_id)
    return jsonify(user), 200
