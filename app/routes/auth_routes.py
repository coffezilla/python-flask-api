# routes/user_routes.py
from flask import Blueprint, request, jsonify
from ..controllers.auth_controller import post_login
from ..utils.decorators import token_required
import jwt
import os
import datetime

auth_bp = Blueprint('auth_bp', __name__)

# POST /login
auth_bp.route('/login', methods=['POST'])(post_login)

# GET /protected


@auth_bp.route('/protected', methods=['GET'])
@token_required
def protected_route():
    return jsonify({'message': 'Access granted to protected route!'}), 200

# POST /refresh-token


@auth_bp.route('/refresh-token', methods=['POST'])
def refresh_token():
    # Get the refresh token from the request body
    refresh_token = request.json.get('refresh_token')
    if not refresh_token:
        return jsonify({'message': 'Refresh token é necessário!'}), 403

    try:
        # Decode the refresh token
        data = jwt.decode(refresh_token, os.getenv(
            'JWT_SECRET'), algorithms=["HS256"])
        user = data['user']
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Refresh token expirado!'}), 403
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Refresh token é inválido!'}), 403

    # Generate a new access token
    new_access_token = jwt.encode({
        'user': user,
        'exp': int((datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=30)).timestamp())
    }, os.getenv('JWT_SECRET'), algorithm="HS256")

    return jsonify({
        'access_token': new_access_token,
        'access_expiration': (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=30)).strftime('%Y-%m-%d %H:%M:%S')
    })
