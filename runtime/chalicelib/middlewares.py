
from chalice import Chalice, Response, ChaliceUnhandledError

def init_middlewares(app: Chalice) -> None:

    def hander_errors(event, get_response) -> Response:
        try:
            return get_response(event)
        except ChaliceUnhandledError as e:
            return Response(
                status_code=500,
                body=str(e),
                headers={'Content-Type': 'text/plain'}
            )



    app.register_middleware(hander_errors, event_type='all')

