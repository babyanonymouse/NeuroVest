# app/bills/routes.py

from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Bill

def register_bills_resources(api):
    """
    Call from create_app:
        register_bills_resources(api)
    """
    api.add_resource(BillList,    '/api/bills')
    api.add_resource(BillResource,'/api/bills/<int:bill_id>')

class BillList(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        bills = Bill.query.filter_by(user_id=user_id).all()
        return [{
            'id': b.id,
            'name': b.name,
            'amount': b.amount,
            'due_date': b.due_date.isoformat(),
            'recurrence_pattern': b.recurrence_pattern
        } for b in bills], 200

    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        data = request.get_json()
        bill = Bill(
            user_id = user_id,
            name    = data['name'],
            amount  = data['amount'],
            due_date= data['due_date'],         # expect YYYY-MM-DD
            recurrence_pattern = data.get('recurrence_pattern')
        )
        db.session.add(bill)
        db.session.commit()
        return {'message': 'Bill created', 'id': bill.id}, 201

class BillResource(Resource):
    @jwt_required()
    def get(self, bill_id):
        user_id = get_jwt_identity()
        bill = Bill.query.filter_by(id=bill_id, user_id=user_id).first_or_404()
        return {
            'id': bill.id,
            'name': bill.name,
            'amount': bill.amount,
            'due_date': bill.due_date.isoformat(),
            'recurrence_pattern': bill.recurrence_pattern
        }, 200

    @jwt_required()
    def put(self, bill_id):
        user_id = get_jwt_identity()
        bill = Bill.query.filter_by(id=bill_id, user_id=user_id).first_or_404()
        data = request.get_json()
        bill.name               = data.get('name', bill.name)
        bill.amount             = data.get('amount', bill.amount)
        bill.due_date           = data.get('due_date', bill.due_date)
        bill.recurrence_pattern = data.get('recurrence_pattern', bill.recurrence_pattern)
        db.session.commit()
        return {'message': 'Bill updated'}, 200

    @jwt_required()
    def delete(self, bill_id):
        user_id = get_jwt_identity()
        bill = Bill.query.filter_by(id=bill_id, user_id=user_id).first_or_404()
        db.session.delete(bill)
        db.session.commit()
        return {'message': 'Bill deleted'}, 200
