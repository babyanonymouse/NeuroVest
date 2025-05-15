# app/goals/routes.py

from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Goal

def register_goals_resources(api):
    """
    Called from create_app:
        register_goals_resources(api)
    """
    api.add_resource(GoalList,    '/api/goals')
    api.add_resource(GoalResource,'/api/goals/<int:goal_id>')

class GoalList(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        goals = Goal.query.filter_by(user_id=user_id).all()
        return [{
            'id': g.id,
            'name': g.name,
            'target_amount': g.target_amount,
            'deadline': g.deadline.isoformat(),
            'progress': g.progress
        } for g in goals], 200

    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        data = request.get_json()
        goal = Goal(
            user_id       = user_id,
            name          = data['name'],
            target_amount = data['target_amount'],
            deadline      = data['deadline'],       # YYYY-MM-DD
            progress      = data.get('progress', 0.0)
        )
        db.session.add(goal)
        db.session.commit()
        return {'message': 'Goal created', 'id': goal.id}, 201

class GoalResource(Resource):
    @jwt_required()
    def get(self, goal_id):
        user_id = get_jwt_identity()
        goal = Goal.query.filter_by(id=goal_id, user_id=user_id).first_or_404()
        return {
            'id': goal.id,
            'name': goal.name,
            'target_amount': goal.target_amount,
            'deadline': goal.deadline.isoformat(),
            'progress': goal.progress
        }, 200

    @jwt_required()
    def put(self, goal_id):
        user_id = get_jwt_identity()
        goal = Goal.query.filter_by(id=goal_id, user_id=user_id).first_or_404()
        data = request.get_json()
        goal.name          = data.get('name', goal.name)
        goal.target_amount = data.get('target_amount', goal.target_amount)
        goal.deadline      = data.get('deadline', goal.deadline)
        goal.progress      = data.get('progress', goal.progress)
        db.session.commit()
        return {'message': 'Goal updated'}, 200

    @jwt_required()
    def delete(self, goal_id):
        user_id = get_jwt_identity()
        goal = Goal.query.filter_by(id=goal_id, user_id=user_id).first_or_404()
        db.session.delete(goal)
        db.session.commit()
        return {'message': 'Goal deleted'}, 200
