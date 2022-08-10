
from chalice import Blueprint, Chalice


databricks_routes = Blueprint(__name__)

@databricks_routes.route('/')
def health():
    return 'ok'
