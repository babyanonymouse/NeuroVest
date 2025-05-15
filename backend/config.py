import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY                = os.environ.get("SECRET_KEY", "super-secret-key")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY            = os.environ.get("JWT_SECRET_KEY", "another-super-secret")

    # Flask-Mail settings
    MAIL_SERVER               = os.environ.get("MAIL_SERVER", "smtp.gmail.com")
    MAIL_PORT                 = int(os.environ.get("MAIL_PORT", 587))
    MAIL_USE_TLS              = os.environ.get("MAIL_USE_TLS", "True").lower() in ["true", "1", "yes"]
    MAIL_USE_SSL              = os.environ.get("MAIL_USE_SSL", "False").lower() in ["true", "1", "yes"]
    MAIL_USERNAME             = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD             = os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER       = os.environ.get("MAIL_DEFAULT_SENDER", MAIL_USERNAME)

class DevConfig(Config):
    DEBUG                     = True
    SQLALCHEMY_DATABASE_URI   = 'sqlite:///' + os.path.join(basedir, 'app.db')

class TestConfig(Config):
    TESTING                   = True
    SQLALCHEMY_DATABASE_URI   = 'sqlite:///:memory:'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI   = os.environ.get('DATABASE_URL')
