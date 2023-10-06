# noqa: E402
from chalice import Blueprint, Chalice, Response
from chalicelib.api.v1.auth import auth_routes
from chalicelib.api.v1.dev import unname_bp
from chalicelib.api.v1.portfolio import porfolio_bp
from chalicelib.api.v1.users import users_blueprints
from chalicelib.config import settings
from chalicelib.events.v1.cognito_events import *
from chalicelib.events.v1.cron_scheduler import *
from chalicelib.events.v1.sns_events import sns_bp
from chalicelib.events.v1.sqs_events import sqs_bp
from chalicelib.logger_app import logger
from chalicelib.utils import export_api_to_json, get_static_file

health_routes = Blueprint(__name__)


@health_routes.route("/health")
def health():
    return "ok"


# Get logger

swagger_api = Blueprint(__name__)


@swagger_api.route("/css", methods=["GET"])
def get_css():
    """Get Swagger UI CSS Endpoint

    Returns:
        str: CSS Content from Static folder
    """
    css_file = "swagger-ui.css"
    logger.info(f"Endpoint: Get CSS : {css_file} static file")
    try:
        content = get_static_file(file_name=css_file)
        return Response(
            body=content,
            status_code=200,
            headers={"Content-Type": "text/css"},
        )
    except Exception as ex:
        return Response(body=f"Failed request: {css_file}. {ex}", status_code=404)


@swagger_api.route("/ui-bundle-js", methods=["GET"])
def get_swagger_ui_bundle():
    """Get Swagger UI Bundle JS Endpoint

    Returns:
        str: Return JavaScript for Swagger UI from static folder
    """
    ui_js_file = "swagger-ui-bundle.js"
    logger.info(f"Endpoint: Get CSS : {ui_js_file} static file")
    content = get_static_file(file_name=ui_js_file)
    try:
        return Response(
            body=content,
            status_code=200,
            headers={"Content-Type": "application/javascript; charset=utf-8"},
        )
    except Exception as ex:
        return Response(body=f"{ui_js_file} not found. {ex}", status_code=404)


@swagger_api.route("/swagger-url", methods=["GET"])
def get_swagger_url():
    return export_api_to_json(swagger_api.current_app)


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
    if settings.ENV == "dev":
        app.register_blueprint(unname_bp, url_prefix="/dev")
    app.register_blueprint(swagger_api)

    # ref:
    #     - https://github.com/aws/chalice/issues/1566
    # app.register_blueprint(dynamodb_bp)
    # app.register_blueprint(cw_bp)
    # app.register_blueprint(s3_bp)
    # app.register_blueprint(cron_bp)
    # app.register_blueprint(sqs_bp)

    return app


events_blueprints = [
    sqs_bp,
    cognito_post_config_bp,
    cronjob_bp,
    sns_bp,
]
