import uuid
from decimal import Decimal

from sqlalchemy import String, Text, UUID, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String(100))
    cpf: Mapped[str] = mapped_column(String(20), unique=True)
    password: Mapped[str] = mapped_column(Text)
    email: Mapped[str] = mapped_column(Text, unique=True)
    saldo: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=0)
    admin: Mapped[bool] = mapped_column(default=False)
