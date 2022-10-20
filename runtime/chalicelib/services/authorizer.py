# from chalice import Chalice, AuthResponse


# def init_auth(app: Chalice):
#     @app.authorizer()
#     def demo_auth(auth_request):
#         token = auth_request.token
#         if token.lower() == "bearer allow":
#             return AuthResponse(routes=["/context", "/", "/today"], principal_id="John Doe")
#         else:
#             return AuthResponse(routes=[], principal_id="unauthorized")