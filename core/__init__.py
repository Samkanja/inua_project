from flask import Flask, request
from core.client.routes import client_views
from core.admin.routes import admin_views, bcrypt
from core.config import DevelopmentConfig, ProductionConfig
from flask_sqlalchemy import SQLAlchemy
from core.models import db, login_manager


# bcrypt = Bcrypt()
# login_manager = LoginManager()
login_manager.login_view = 'admin.login'

def config_all(app):
     if app.debug:
          app.config.from_object(DevelopmentConfig)
     else:
          app.config.from_object(ProductionConfig)
          
     db.init_app(app)
     bcrypt.init_app(app)
     login_manager.init_app(app)

     config_database(app)
     config_route(app)
     return app


def config_route(app):
    app.register_blueprint(client_views)
    app.register_blueprint(admin_views)

def config_database(app):
     from core import models
     with app.app_context():
          db.create_all()