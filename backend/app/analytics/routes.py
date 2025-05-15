# app/analytics/routes.py

from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.analytics.engine import analyze_spending, forecast_health
from app.services.advice import generate_advice

def register_analytics_resources(api):
    """
    Called from create_app:
        register_analytics_resources(api)
    """
    api.add_resource(SpendingAnalysis, '/api/analytics/spending')
    api.add_resource(Forecast,         '/api/analytics/forecast')
    api.add_resource(GoalAdvice,       '/api/analytics/advice')

class SpendingAnalysis(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        period = request.args.get('period', 'monthly')
        result = analyze_spending(user_id, period)
        return result, 200

class Forecast(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        horizon = request.args.get('horizon', '6_months')
        result = forecast_health(user_id, horizon)
        return result, 200

class GoalAdvice(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        goal_id = request.args.get('goal_id')
        advice = generate_advice(user_id, goal_id)
        return {'advice': advice}, 200
