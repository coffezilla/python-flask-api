from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# routes
from .routes.users_routes import users_bp
from .routes.posts_routes import posts_bp

# models
# from app.models import *
from app.models import db
from app.models.users import Users
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
        app.register_blueprint(users_bp)
        app.register_blueprint(posts_bp)

        if os.getenv('FLASK_ENV') == 'development':
            print("This is dev")
            db.create_all()

    return app
