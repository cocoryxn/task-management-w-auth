from pydantic import BaseModel, Field
from uuid import UUID

from app.modules.tasks.models import TaskStatus

class CreateTask(BaseModel):
    task_title : str = Field(min_length=0, max_length=30, default="Untitled")
    task_body : str | None = None
    task_status : str = Field(default=TaskStatus.TODO)

class UpdateTaskTitleBody(BaseModel):
    task_title : str = Field(min_length=0, max_length=30)
    task_body : str | None = None
    task_status : TaskStatus

class CreatedTaskResponse(CreateTask):
    id : UUID
    # created_at : datetime
    # updated_at : datetime
    pass

