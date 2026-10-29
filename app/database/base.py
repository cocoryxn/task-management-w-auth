from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from uuid import uuid4, UUID

from sqlalchemy import UUID as SQLITE_UUID
class Base(DeclarativeBase):
    pass


class UUIDMixing:
    id : Mapped[UUID] = mapped_column(
        SQLITE_UUID(as_uuid=True),
        primary_key=True,
        default=uuid4
    )
