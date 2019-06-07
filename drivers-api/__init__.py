from flask import Flask
from . import routes


def create_app():

    app = Flask(__name__, instance_relative_config=True)

    app.register_blueprint(routes.bp_main)

    app.register_blueprint(routes.bp_source)
    app.register_blueprint(routes.bp_shutter)
    app.register_blueprint(routes.bp_motor)

    @app.after_request
    def after_request(response):
        header = response.headers
        header['Content-Type'] = 'application/json; charset=utf-8'
        return response

    return app
