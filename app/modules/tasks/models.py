from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, Enum as StatusEnum

from enum import Enum

from app.database.base import Base, UUIDMixing

class TaskStatus(str, Enum):
    TODO = "Todo"
    IN_PROGRESS = "In progress"
    DONE = "Done"

class Task(Base, UUIDMixing):
    __tablename__="task"

    task_title : Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    task_body : Mapped[str] = mapped_column(
        String(255),
        nullable=True 
    )

    task_status : Mapped[str] = mapped_column(
        StatusEnum(TaskStatus, name = "task_status"),
        default=TaskStatus.TODO,
        nullable=False
    )