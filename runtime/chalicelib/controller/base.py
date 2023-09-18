# from dataclasses import dataclass
# from typing import Protocol

# from botocore.exceptions import ClientError
# from chalicelib.events.base import EventType, post_event
# from chalicelib.logger_app import logger
# from chalicelib.schemas import UserCreate, UserSignIn
# from chalicelib.services.authorizers import Authenticator
# from chalicelib.services.authorizers import authenticator as current_authenticator


# class BatchAPI(Protocol):
#     decorators = [login_required]

#     # @swag_from(f"openapi/apidocs/{name}_get_all.yaml")
#     def get(self):
#         security.check_auth(cls, "R")
#         query = GET_query(cls)

#         if hasattr(cls, "valid_to_show"):
#             query = query.filter(cls.valid_to_show)

#         log_event(cls.__entity_name__)
#         return GET_postprocess(cls, query)

#     # @swag_from(f"openapi/apidocs/{name}_post.yaml")
#     def post(self):
#         utils.require_json()
#         new_pk = insert_data(cls, request.get_json(), aliases=True)
#         db.session.commit()
#         perform_actions_after_request(cls, request.get_json())
#         return GET_one_fn(cls, new_pk, GET_query(cls))


# class InstanceAPI:
#     decorators = [login_required]

#     @swag_from(f"openapi/apidocs/{name}_put.yaml")
#     def patch(self, id):
#         utils.require_json()
#         update_data(cls, request.get_json(), id)
#         db.session.commit()
#         perform_actions_after_request(cls, request.get_json(), id)
#         return self.get(id)

#     @swag_from(f"openapi/apidocs/{name}_put.yaml")
#     def put(self, id):
#         return self.patch(id)

#     @swag_from(f"openapi/apidocs/{name}_get.yaml")
#     def get(self, id):
#         security.check_auth(cls, "R")
#         return GET_one_fn(cls, id, GET_query(cls))

#     @swag_from(f"openapi/apidocs/{name}_delete.yaml")
#     def delete(self, id):
#         security.check_auth(cls, "D", id)

#         statement = (
#             cls.__table__.update()
#             .values(
#                 f_changedby=current_user.id,
#                 deleted="T",
#             )
#             .where(sa.and_(cls.id == id, cls.deleted == "F"))
#         )
#         x = execute_statement(cls, statement)
#         if x.rowcount > 0:
#             db.session.commit()
#             perform_actions_after_request(cls, {"deleted": True}, id)
#             return "", 204
#         else:
#             return "No such id\n", 404
