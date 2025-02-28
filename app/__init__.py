from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# routes
from .routes.user_routes import user_bp
from .routes.posts_routes import posts_bp
from .routes.auth_routes import auth_bp

# models
# from app.models import *
from app.models import db
from app.models.user import User
from app.models.posts import Posts


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate = Migrate(app, db)

    @app.route('/')
    def home():
        return {"message": "API Hello World"}

    with app.app_context():
        app.register_blueprint(user_bp)
        app.register_blueprint(posts_bp)
        app.register_blueprint(auth_bp)

        if os.getenv('FLASK_ENV') == 'development':
            print("This is dev")
            db.create_all()

    return app
