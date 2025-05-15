from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Expense

def register_expenses_resources(api):
    api.add_resource(ExpenseList,    '/api/expenses')
    api.add_resource(ExpenseResource,'/api/expenses/<int:expense_id>')

class ExpenseList(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        expenses = Expense.query.filter_by(user_id=user_id).all()
        return [ {
            'id': e.id,
            'amount': e.amount,
            'category': e.category,
            'date': e.date.isoformat(),
            'recurring': e.recurring
        } for e in expenses ], 200

    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        data = request.get_json()
        expense = Expense(
            user_id  = user_id,
            amount   = data['amount'],
            category = data['category'],
            date     = data.get('date'),       # expect YYYY-MM-DD or omit for today
            recurring= data.get('recurring', False)
        )
        db.session.add(expense)
        db.session.commit()
        return {'message': 'Expense created', 'id': expense.id}, 201

class ExpenseResource(Resource):
    @jwt_required()
    def get(self, expense_id):
        user_id = get_jwt_identity()
        expense = Expense.query.filter_by(id=expense_id, user_id=user_id).first_or_404()
        return {
            'id': expense.id,
            'amount': expense.amount,
            'category': expense.category,
            'date': expense.date.isoformat(),
            'recurring': expense.recurring
        }, 200

    @jwt_required()
    def put(self, expense_id):
        user_id = get_jwt_identity()
        expense = Expense.query.filter_by(id=expense_id, user_id=user_id).first_or_404()
        data = request.get_json()
        expense.amount    = data.get('amount', expense.amount)
        expense.category  = data.get('category', expense.category)
        expense.date      = data.get('date', expense.date)
        expense.recurring = data.get('recurring', expense.recurring)
        db.session.commit()
        return {'message': 'Expense updated'}, 200

    @jwt_required()
    def delete(self, expense_id):
        user_id = get_jwt_identity()
        expense = Expense.query.filter_by(id=expense_id, user_id=user_id).first_or_404()
        db.session.delete(expense)
        db.session.commit()
        return {'message': 'Expense deleted'}, 200
