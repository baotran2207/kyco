from sqlalchemy.ext.declarative import as_declarative, declared_attr

# class MinBase:
#     pass


@as_declarative()
class Base(object):
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()
