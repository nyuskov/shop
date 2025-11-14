from typing import TYPE_CHECKING

from sqlalchemy import String  # type: ignore
from sqlalchemy.orm import relationship, Mapped, mapped_column  # type: ignore

from .base import Base
from .mixins import IdIntPkMixin

if TYPE_CHECKING:
    from .product import Product


class Category(IdIntPkMixin, Base):
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    slug: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    products: Mapped[list["Product"]] = relationship(
        "Product",
        back_populates="category",
    )

    def __repr__(self) -> str:
        return f"<Category(name={self.name}, slug={self.slug})>"
