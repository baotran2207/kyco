
from chalice import Blueprint, Chalice

from chalicelib.api.v1.auth import auth_routes
from chalicelib.api.v1.users import users_blueprints

# from chalicelib.events.v1.cron_scheduler import cron_bp
# from chalicelib.events.v1.sqs_events import sqs_bp

health_routes = Blueprint(__name__)


@health_routes.route('/')
def health():
    return 'ok'

def init_blueprint(app: Chalice):
    """
     - https://github.com/aws/chalice/issues/1566
    Currently register_blueprint only work with api but events and pure function.

    """
    # v1
    app.register_blueprint(health_routes, url_prefix='/v1')
    # app.register_blueprint(auth_routes, url_prefix='/v1/auth')
    # app.register_blueprint(users_blueprints, url_prefix='/v1')



    # ref:
    #     - https://github.com/aws/chalice/issues/1566
    # app.register_blueprint(dynamodb_bp)
    # app.register_blueprint(cw_bp)
    # app.register_blueprint(s3_bp)
    # app.register_blueprint(cron_bp)
    # app.register_blueprint(sqs_bp)


    return app

