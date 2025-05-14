# resources.py
from flask_restful import Resource
from flask import request, jsonify
from models import db, User
from flask_jwt_extended import jwt_required

class UserListResource(Resource):
    # GET all users
    def get(self):
        users = User.query.all()
        return jsonify([user.serialize() for user in users])

    # POST a new user
    def post(self):
        data = request.get_json()
        
        if not data or not data.get('username') or not data.get('password'):
            return jsonify({"message": "Missing required fields"}), 400

        new_user = User(
            username=data['username'],
            password=data['password']  # Don't forget hashing in production!
        )

        db.session.add(new_user)
        db.session.commit()

        return jsonify(new_user.serialize()), 201


class UserResource(Resource):
    # GET a single user by ID
    @jwt_required()
    def get(self, id):
        user = User.query.get_or_404(id)
        return jsonify(user.serialize())

    # PUT to update an existing user
    @jwt_required()
    def put(self, id):
        data = request.get_json()
        user = User.query.get_or_404(id)

        user.username = data['username']
        user.password = data['password']  # Update logic here (hash password before saving)
        db.session.commit()

        return jsonify(user.serialize())

    # DELETE a user
    @jwt_required()
    def delete(self, id):
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"}), 204  # Return a JSON message for clarity
