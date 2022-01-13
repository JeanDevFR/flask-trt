from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
mail = Mail()
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.login_message = "Veuillez vous connecter pour accéder à cette page."
login_manager.login_message_category = "warning"


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from app.auth.routes import auth
    from app.jobs.routes import jobs
    from app.main.routes import main
    from app.admin.routes import admin
    from app.account.routes import account

    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(jobs)
    app.register_blueprint(admin)
    app.register_blueprint(account)

    return app