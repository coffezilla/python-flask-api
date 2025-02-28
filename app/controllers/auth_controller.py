# controllers/user_controller.py
from flask import jsonify, request
from ..services.auth_service import post_login_service


def post_login():
    new_login = post_login_service()
    return jsonify(new_login), 201
