# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_restful import Api, Resource
from flask_cors import CORS
from config import Config
from models import db, User
from resources import UserListResource, UserResource

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)
    jwt = JWTManager(app)
    CORS(app)

    api = Api(app)

    # Add resources to the API
    api.add_resource(UserListResource, '/users')      # Route for list of users
    api.add_resource(UserResource, '/user/<int:id>')  # Route for single user (GET, PUT, DELETE)

    return app

app = create_app()
