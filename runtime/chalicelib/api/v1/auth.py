
from chalice import Blueprint


auth_routes = Blueprint(__name__)

@auth_routes.route('/login')
def login():
    return 'About to login'


# @auth_routes.route('/register')
# def register():
#     pass

