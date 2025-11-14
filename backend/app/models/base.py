from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(DeclarativeBase, AsyncAttrs):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        tablename = cls.__name__.lower()

        if tablename[-1] == "y":
            return f"{tablename[:-1]}ies"
        else:
            return f"{tablename}s"
