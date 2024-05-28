from core.client.routes import client_views

def config_all(app):
     app.config["SECRET_KEY"] = "asdjkakdjkadakdjkakdka"
     config_route(app)
     return app


def config_route(app):
    app.register_blueprint(client_views)