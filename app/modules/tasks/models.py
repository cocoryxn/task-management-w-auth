from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, Enum as StatusEnum

from enum import Enum

from app.database.base import Base

class TaskStatus(str, Enum):
    TODO = "Todo"
    IN_PROGRESS = "In progress"
    DONE = "Done"

class Task(Base):
    __tablename__="task"

    task_no : Mapped[str] = mapped_column(
        String(10),
        unique=True,
        index=True,
        primary_key=True,
    )

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