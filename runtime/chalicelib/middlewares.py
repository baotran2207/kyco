from aws_lambda_powertools import Logger
from chalice import Chalice, ChaliceUnhandledError, Response
from chalice.app import ConvertToMiddleware
from chalicelib.logger_app import logger

# This will automatically convert any decorator on a lambda function
# into middleware that will be connected to every lambda function
# in our app.  This lets us avoid decoratoring every lambda function
# with this behavior, but it also works in cases where we don't control
# the code (e.g. registering blueprints).


def init_middlewares(app: Chalice) -> None:
    logger_power = Logger(service=app.app_name)

    def hander_errors(event, get_response) -> Response:
        response = get_response(event)
        status_code = response.status_code
        body = response.body
        event_values = event.to_dict()
        try:
            if status_code >= 500:
                logger.error(
                    f"Event : {event_values} . Response: {status_code} - {body}"
                )
            return response
        except ChaliceUnhandledError as e:
            return Response(
                status_code=500, body=str(e), headers={"Content-Type": "text/plain"}
            )

    def http_errors(event, get_response) -> Response:
        try:
            return get_response(event)
        except ChaliceUnhandledError as e:
            return Response(
                status_code=500, body=str(e), headers={"Content-Type": "text/plain"}
            )

    app.register_middleware(ConvertToMiddleware(logger_power.inject_lambda_context))
    app.register_middleware(hander_errors, event_type="all")
