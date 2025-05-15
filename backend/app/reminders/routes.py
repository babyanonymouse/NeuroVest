# app/reminders/routes.py

from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Reminder

def register_reminders_resources(api):
    """
    Called from create_app:
        register_reminders_resources(api)
    """
    api.add_resource(ReminderList,    '/api/reminders')
    api.add_resource(ReminderResource,'/api/reminders/<int:reminder_id>')

class ReminderList(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        reminders = Reminder.query.filter_by(user_id=user_id).all()
        return [{
            'id': r.id,
            'type': r.type,
            'target_id': r.target_id,
            'remind_at': r.remind_at.isoformat(),
            'sent_flag': r.sent_flag
        } for r in reminders], 200

    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        data = request.get_json()
        reminder = Reminder(
            user_id   = user_id,
            type      = data['type'],
            target_id = data.get('target_id'),
            remind_at = data['remind_at']  # expect ISO datetime string
        )
        db.session.add(reminder)
        db.session.commit()
        return {'message': 'Reminder created', 'id': reminder.id}, 201

class ReminderResource(Resource):
    @jwt_required()
    def get(self, reminder_id):
        user_id = get_jwt_identity()
        reminder = Reminder.query.filter_by(id=reminder_id, user_id=user_id).first_or_404()
        return {
            'id': reminder.id,
            'type': reminder.type,
            'target_id': reminder.target_id,
            'remind_at': reminder.remind_at.isoformat(),
            'sent_flag': reminder.sent_flag
        }, 200

    @jwt_required()
    def delete(self, reminder_id):
        user_id = get_jwt_identity()
        reminder = Reminder.query.filter_by(id=reminder_id, user_id=user_id).first_or_404()
        db.session.delete(reminder)
        db.session.commit()
        return {'message': 'Reminder deleted'}, 200
