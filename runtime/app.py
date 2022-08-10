
from chalice import Chalice
from chalicelib.config import settings ## loadsetting before start up
from chalicelib.blueprint import init_blueprint
from chalicelib.middlewares import init_middlewares

app = Chalice(app_name='chalice-backend')


init_blueprint(app)
init_middlewares(app)