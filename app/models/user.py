from . import db
import bcrypt
from ..utils.token import generate_token
from ..schemas.user_schema import UserSchema


class User(db.Model):
    # __tablename__ = 'users'

    id = db.Column(db.String(36), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=True)

    def __repr__(self):
        return f'<User {self.username}>'

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
        }

    def post_to_dict(self, password):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': password
        }

    def token_to_dict(self):
        new_token = generate_token(self.email)
        return {
            'id': self.id,
            'email': self.email,
            'access_token': new_token["access_token"],
            'access_expiration': new_token["access_expiration"],
            'refresh_token': new_token["refresh_token"],
            'refresh_expiration': new_token["refresh_expiration"]
        }

    def set_password(self, plain_password):
        plain_password_b = plain_password.encode('utf-8')

        self.password = bcrypt.hashpw(
            plain_password_b, bcrypt.gensalt()).decode('utf-8')

    def check_password(self, plain_password):
        plain_password_b = plain_password.encode('utf-8')
        self_password_b = self.password.encode('utf-8')

        return bcrypt.checkpw(plain_password_b, self_password_b)
