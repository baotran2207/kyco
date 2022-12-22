# from sqlalchemy.orm import Session
# from chalice
# # from app import crud, schemas
# from chalicelib.config import settings
# from chalicelib.db.session import SessionLocal
# from chalicelib.db import base
# from chalicelib.schemas import UserCreate


# def init_db(db: Session, settings):
#     first_user = user.get_by_email(db, email=settings.WEBMASTER_EMAIL)

#     if not first_user:
#         init_user = UserCreate(
#             email=settings.WEBMASTER_EMAIL,
#             password=settings.WEBMASTER_PASSWORD,
#             is_superuser=True,
#         )
#         new_user = user.create(db, obj_to_create=init_user)  # noqa: F841
#         print(new_user)

#     # logger.info("The first user was created ")
#     return first_user


# if __name__ == "__main__":
#     db = SessionLocal()
#     init_db(db, settings)
