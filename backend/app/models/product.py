from datetime import datetime, timezone

from sqlalchemy import (  # type: ignore
    DateTime,
    ForeignKey,
    String,
    Text,
    Integer,
)
from sqlalchemy.orm import relationship, Mapped, mapped_column  # type: ignore

from .base import Base
from .mixins import IdIntPkMixin


class Product(IdIntPkMixin, Base):
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    category_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("categories.id"),
        nullable=False,
    )
    image_url: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(timezone.utc),
    )
    category = relationship("Category", back_populates="products")

    def __repr__(self) -> str:
        return f"<Product(id={self.id}, name={self.name}, price={self.price})>"
