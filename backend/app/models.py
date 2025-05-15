# app/models.py

from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    id             = db.Column(db.Integer, primary_key=True)
    email          = db.Column(db.String(120), unique=True, nullable=False)
    password_hash  = db.Column(db.String(128), nullable=False)
    created_at     = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    expenses       = db.relationship('Expense',     back_populates='user', lazy='dynamic')
    bills          = db.relationship('Bill',        back_populates='user', lazy='dynamic')
    goals          = db.relationship('Goal',        back_populates='user', lazy='dynamic')
    score_history  = db.relationship('ScoreHistory',back_populates='user', lazy='dynamic')
    reminders      = db.relationship('Reminder',    back_populates='user', lazy='dynamic')

    def set_password(self, password):
        from werkzeug.security import generate_password_hash
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password_hash, password)


class Expense(db.Model):
    __tablename__ = 'expenses'

    id        = db.Column(db.Integer, primary_key=True)
    user_id   = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    amount    = db.Column(db.Float, nullable=False)
    category  = db.Column(db.String(64), nullable=False)
    date      = db.Column(db.Date, default=datetime.utcnow, nullable=False)
    recurring = db.Column(db.Boolean, default=False)

    user      = db.relationship('User', back_populates='expenses')


class Bill(db.Model):
    __tablename__ = 'bills'

    id                 = db.Column(db.Integer, primary_key=True)
    user_id            = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name               = db.Column(db.String(128), nullable=False)
    amount             = db.Column(db.Float, nullable=False)
    due_date           = db.Column(db.Date, nullable=False)
    recurrence_pattern = db.Column(db.String(32), nullable=True)  # e.g., 'monthly', 'yearly'

    user               = db.relationship('User', back_populates='bills')


class Goal(db.Model):
    __tablename__ = 'goals'

    id             = db.Column(db.Integer, primary_key=True)
    user_id        = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name           = db.Column(db.String(128), nullable=False)
    target_amount  = db.Column(db.Float, nullable=False)
    deadline       = db.Column(db.Date, nullable=False)
    progress       = db.Column(db.Float, default=0.0)

    user           = db.relationship('User', back_populates='goals')


class ScoreHistory(db.Model):
    __tablename__ = 'score_history'

    id             = db.Column(db.Integer, primary_key=True)
    user_id        = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    score          = db.Column(db.Float, nullable=False)
    date_recorded  = db.Column(db.DateTime, default=datetime.utcnow)

    user           = db.relationship('User', back_populates='score_history')


class Reminder(db.Model):
    __tablename__ = 'reminders'

    id         = db.Column(db.Integer, primary_key=True)
    user_id    = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    type       = db.Column(db.String(32), nullable=False)  # e.g., 'expense', 'bill', 'goal'
    target_id  = db.Column(db.Integer, nullable=True)      # which expense/bill/goal to remind about
    remind_at  = db.Column(db.DateTime, nullable=False)
    sent_flag  = db.Column(db.Boolean, default=False)

    user       = db.relationship('User', back_populates='reminders')
