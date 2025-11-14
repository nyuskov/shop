from sqlalchemy.orm import (  # type: ignore
    Mapped,
    mapped_column,
)


class IdIntPkMixin:
    id: Mapped[int] = mapped_column(primary_key=True)
