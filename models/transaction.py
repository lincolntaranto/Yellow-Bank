from datetime import datetime
import uuid

from decimal import Decimal
from sqlalchemy import (
    UUID as SA_UUID,
    ForeignKey,
    DateTime,
    Numeric,
    func,
    CheckConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column

from models import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[uuid.UUID] = mapped_column(
        SA_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    payer: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    payee: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    # Eu futuro, lembre de usar Decimal ao invés de float para dinheiro.
    value: Mapped[Decimal] = mapped_column(Numeric(12, 2))
    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    __table_args__ = (
        CheckConstraint("value > 0", name="ck_value_positive"),
        CheckConstraint("payer != payee", name="ck_payer_payee_diff"),
    )
