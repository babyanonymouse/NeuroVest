# app/auth/routes.py
from flask import request
from flask_restful import Resource
from app.models import User
from app import db
from flask_jwt_extended import create_access_token

def register_auth_resources(api):
    """
    Call this from create_app:
        register_auth_resources(api)
    """
    api.add_resource(Register, '/api/auth/register')
    api.add_resource(Login,    '/api/auth/login')

class Register(Resource):
    def post(self):
        data = request.get_json()
        if not data or not data.get('email') or not data.get('password'):
            return {'message': 'Email and password required'}, 400

        if User.query.filter_by(email=data['email']).first():
            return {'message': 'Email already registered'}, 400

        user = User(email=data['email'])
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return {'message': 'User created'}, 201

class Login(Resource):
    def post(self):
        data = request.get_json()
        if not data or not data.get('email') or not data.get('password'):
            return {'message': 'Email and password required'}, 400

        user = User.query.filter_by(email=data['email']).first()
        if not user or not user.check_password(data['password']):
            return {'message': 'Bad credentials'}, 401

        access_token = create_access_token(identity=user.id)
        return {'access_token': access_token}, 200
