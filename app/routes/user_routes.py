# routes/user_routes.py
from flask import Blueprint, request
from ..controllers.user_controller import get_users, get_user_by_id, post_user, delete_user, patch_user

user_bp = Blueprint('user_bp', __name__)

# GET /users
user_bp.route('/users', methods=['GET'])(get_users)

# GET /users/<id>
user_bp.route('/users/<user_id>', methods=['GET'])(get_user_by_id)

# POST /users
user_bp.route('/users', methods=['POST'])(post_user)

# DELETE /users/<id>
user_bp.route('/users/<user_id>', methods=['DELETE'])(delete_user)

# PATCH /users/<id>
user_bp.route('/users/<user_id>', methods=['PATCH'])(patch_user)
