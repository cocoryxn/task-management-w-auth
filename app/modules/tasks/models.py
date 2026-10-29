import uuid
from enum import Enum

from typing import TYPE_CHECKING
from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
if TYPE_CHECKING:
    from app.modules.users.models import User


class TaskStatus(str, Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"


class Task(Base):
    __tablename__ = "task"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

    task_title: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    task_body: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    task_status: Mapped[TaskStatus] = mapped_column(
        SQLAlchemyEnum(TaskStatus, name="task_status"),
        default=TaskStatus.TODO,
        nullable=False,
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    user: Mapped["User"] = relationship(
        back_populates="tasks",
    )