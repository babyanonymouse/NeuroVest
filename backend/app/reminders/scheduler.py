# app/reminders/scheduler.py

from datetime import datetime
from flask_mail import Message
from app import db, mail
from app.models import Reminder, User

def send_due_reminders(app):
    """
    Query all reminders where:
      - remind_at ≤ now
      - sent_flag is False
    Send an email for each, then mark sent_flag=True.
    """
    with app.app_context():
        now = datetime.utcnow()
        due = (
            Reminder.query
            .filter(Reminder.remind_at <= now, Reminder.sent_flag == False)
            .all()
        )

        for rem in due:
            user = User.query.get(rem.user_id)
            if not user:
                continue

            # Construct a simple email
            subject = f"Reminder: {rem.type.capitalize()} #{rem.target_id or rem.id}"
            body    = (
                f"Hi,\n\n"
                f"This is your reminder for {rem.type} "
                f"(ID: {rem.target_id or rem.id}) scheduled at {rem.remind_at} UTC.\n\n"
                "Best,\nYour Finance AI"
            )

            msg = Message(
                subject=subject,
                recipients=[user.email],
                body=body
            )

            try:
                mail.send(msg)
                rem.sent_flag = True
                db.session.add(rem)
            except Exception as e:
                app.logger.error(f"Failed to send reminder {rem.id}: {e}")

        db.session.commit()
