from core.admin.routes import admins, bcrypt
from core.client.routes import client
from core.config import Config
from core.models import db, Admin, Program, login_manager


login_manager.login_view = "admins.login"


def config_all(app):
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    create_db(app)
    config_routes(app)
    return app


def config_routes(app):
    app.register_blueprint(admins)
    app.register_blueprint(client)


def create_db(app):
    from core import models

    with app.app_context():
        db.create_all()
