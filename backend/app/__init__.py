# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_jwt_extended import JWTManager
# from flask_cors import CORS
# from flask_restful import Api
# from flask_mail import Mail
# from apscheduler.schedulers.background import BackgroundScheduler

# db        = SQLAlchemy()
# migrate   = Migrate()
# jwt       = JWTManager()
# mail      = Mail()
# scheduler = BackgroundScheduler()

# def create_app(config_class="config.DevConfig"):
#     app = Flask(__name__)
#     app.config.from_object(config_class)

#     # Extensions
#     CORS(app)
#     db.init_app(app)
#     migrate.init_app(app, db)
#     jwt.init_app(app)
#     mail.init_app(app)

#     # REST API
#     api = Api(app)

#     # Register Resources via registration functions
#     from app.auth.routes      import register_auth_resources
#     from app.expenses.routes  import register_expenses_resources
#     from app.bills.routes     import register_bills_resources
#     from app.goals.routes     import register_goals_resources
#     from app.analytics.routes import register_analytics_resources
#     from app.reminders.routes import register_reminders_resources

#     register_auth_resources(api)
#     register_expenses_resources(api)
#     register_bills_resources(api)
#     register_goals_resources(api)
#     register_analytics_resources(api)
#     register_reminders_resources(api)

#     # Scheduler setup: send reminders every minute
#     from app.reminders.scheduler import send_due_reminders
#     scheduler.add_job(
#         func=lambda: send_due_reminders(app),
#         trigger='interval',
#         minutes=1,
#         id='reminder_job',
#         replace_existing=True
#     )
#     scheduler.start()

#     # Ensure scheduler shuts down cleanly
#     @app.teardown_appcontext
#     def shutdown_scheduler(exception=None):
#         scheduler.shutdown(wait=False)

#     return app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_restful import Api
from flask_mail import Mail
from apscheduler.schedulers.background import BackgroundScheduler

db        = SQLAlchemy()
migrate   = Migrate()
jwt       = JWTManager()
mail      = Mail()
scheduler = BackgroundScheduler()

def create_app(config_class="config.DevConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Extensions
    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    mail.init_app(app)

    # REST API
    api = Api(app)

    # Register Resources via registration functions
    from app.auth.routes      import register_auth_resources
    from app.expenses.routes  import register_expenses_resources
    from app.bills.routes     import register_bills_resources
    from app.goals.routes     import register_goals_resources
    from app.analytics.routes import register_analytics_resources
    from app.reminders.routes import register_reminders_resources

    register_auth_resources(api)
    register_expenses_resources(api)
    register_bills_resources(api)
    register_goals_resources(api)
    register_analytics_resources(api)
    register_reminders_resources(api)

    # Scheduler setup: send reminders every minute
    from app.reminders.scheduler import send_due_reminders
    scheduler.add_job(
        func=lambda: send_due_reminders(app),
        trigger='interval',
        minutes=1,
        id='reminder_job',
        replace_existing=True
    )
    scheduler.start()

    # Ensure scheduler shuts down cleanly if it was started
    @app.teardown_appcontext
    def shutdown_scheduler(exception=None):
        if scheduler.running:
            scheduler.shutdown(wait=False)

    return app
