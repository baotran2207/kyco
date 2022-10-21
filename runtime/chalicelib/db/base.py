# Import all the models, so that Base has them before being
# imported by Alembic
from chalicelib.db.base_class import Base  # noqa
from chalicelib.models import User, UsedToken # noqa
