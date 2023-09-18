# noqa: E402
from chalice import Blueprint, Chalice
from chalicelib.api.v1.auth import auth_routes
from chalicelib.api.v1.dev import unname_bp
from chalicelib.api.v1.portfolio import porfolio_bp
from chalicelib.api.v1.users import users_blueprints
from chalicelib.config import settings
from chalicelib.events.v1.cognito_events import *
from chalicelib.events.v1.cron_scheduler import *
from chalicelib.events.v1.sns_events import sns_bp
from chalicelib.events.v1.sqs_events import sqs_bp

health_routes = Blueprint(__name__)


@health_routes.route("/health")
def health():
    return "ok"


def init_blueprint(app: Chalice):
    """
     - https://github.com/aws/chalice/issues/1566
    Currently register_blueprint only work with api but events and pure function.

    """
    # v1
    app.register_blueprint(health_routes)
    app.register_blueprint(auth_routes, url_prefix="/auth")
    app.register_blueprint(users_blueprints)

    app.register_blueprint(porfolio_bp, url_prefix="/porfolio")
    # if settings.ENV == "dev":
    app.register_blueprint(unname_bp, url_prefix="/dev")

    # ref:
    #     - https://github.com/aws/chalice/issues/1566
    # app.register_blueprint(dynamodb_bp)
    # app.register_blueprint(cw_bp)
    # app.register_blueprint(s3_bp)
    # app.register_blueprint(cron_bp)
    # app.register_blueprint(sqs_bp)

    return app


events_blueprints = [sqs_bp, cognito_post_config_bp, cronjob_bp, sns_bp]
