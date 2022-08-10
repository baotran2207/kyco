
from chalice import Blueprint, Chalice

from chalicelib.api.v1.auth import auth_routes
from chalicelib.api.v1.users import users_blueprints


from chalicelib.events.v1.cloudwatch_events import cw_bp
from chalicelib.events.v1.dynamodb_events import dynamodb_bp
from chalicelib.events.v1.s3_events import s3_bp

health_routes = Blueprint(__name__)

@health_routes.route('/')
def health():
    return 'ok'

def init_blueprint(app: Chalice):
    # v1
    app.register_blueprint(health_routes, url_prefix='/v1')
    app.register_blueprint(auth_routes, url_prefix='/v1/auth')
    app.register_blueprint(users_blueprints, url_prefix='/v1')

    app.register_blueprint(dynamodb_bp)
    app.register_blueprint(cw_bp)
    app.register_blueprint(s3_bp)

    return app

