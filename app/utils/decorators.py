from flask import request, jsonify
import jwt
import os
from functools import wraps


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Get the Authorization header
        auth_header = request.headers.get('Authorization')
        print(auth_header)
        if not auth_header:
            return jsonify({'message': 'Token é necessário!'}), 403

        # Extract the token from the header
        try:
            # Get the token part after 'Bearer'
            token = auth_header.split(" ")[1]
        except IndexError:
            return jsonify({'message': 'Token é necessário!'}), 403

        try:
            data = jwt.decode(token, os.getenv(
                'JWT_SECRET'), algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expirado!'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token é inválido!'}), 403

        return f(*args, **kwargs)
    return decorated
