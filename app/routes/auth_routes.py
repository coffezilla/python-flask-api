# routes/user_routes.py
from flask import Blueprint, request, jsonify
from ..controllers.auth_controller import post_login
# Import the token_required decorator
from ..utils.decorators import token_required

auth_bp = Blueprint('auth_bp', __name__)


# POST /login
auth_bp.route('/login', methods=['POST'])(post_login)

# GET /protected


@auth_bp.route('/protected', methods=['GET'])
@token_required
def protected_route():
    return jsonify({'message': 'Access granted to protected route!'}), 200
