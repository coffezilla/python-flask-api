from flask import jsonify, request
import uuid
from ..models.user import User
from ..utils.uuid import is_valid_uuid
from ..models import db


# post
def post_login_service():
    # pega os dados do usuário
    # schema = UserSchema()
    data = request.get_json()

    # verifica se tem campos de login
    if not data or 'email' not in data or 'password' not in data:
        return {"message": "Missing some attribute"}

    # faz a busca do usuario
    user = User.query.filter_by(email=data['email']).first()
    if user and user.check_password(data['password']):

        return {
            'user': user.token_to_dict()
        }
    else:
        return {"message": "Wrong password"}

    # verifica se o login bate

    # retorna o novo token
    # return {"message": "Login"}
    # schema = UserSchema()
    # data = request.get_json()

    # try:
    #     user_data = schema.load(data)
    # except Exception as e:
    #     return {"message": "schema error", "error": str(e)}, 400

    # # after the schema, this is not important
    # # if not data or 'username' not in data or 'email' not in data:
    # #     return {"message": "Missing some attribute"}

    # new_user = User(
    #     id=str(uuid.uuid4()),  # Use UUID for user ID
    #     username=user_data['username'],
    #     email=user_data['email'],
    # )

    # db.session.add(new_user)
    # db.session.commit()

    # return schema.dump(new_user.to_dict())
