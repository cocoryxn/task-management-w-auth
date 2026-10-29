from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from uuid import uuid4

from app.modules.tasks.schemas import (
    CreateTask, 
    CreatedTaskResponse,
    UpdateTaskTitleBody
)
from app.modules.tasks.models import Task
from app.database.session import get_session

router = APIRouter(prefix="/tasks", tags=["Task"])

@router.get("/")
def get_task():
    return {"massage":"getting task"}

@router.post("/", response_model=CreatedTaskResponse)
def create_task( payload : CreateTask , session : Session = Depends(get_session)) -> Task:

    task = Task(
        task_title=payload.task_title,
        task_body=payload.task_body,
        task_status=payload.task_status,
    )

    session.add(task)
    session.commit()
    session.refresh(task)

    return task

@router.get("/{task_no}", response_model=CreatedTaskResponse)
def read_task(task_title : str, session : Session = Depends(get_session)) -> Task:
    task = (session.execute(select(Task).where(Task.task_title == task_title))).scalar_one_or_none()
    return task


@router.patch("/{task_no}", response_model=CreatedTaskResponse)
def update_task(task_no : uuid4, update_payload : UpdateTaskTitleBody , session : Session = Depends(get_session)) -> Task:
    task = (session.execute(select(Task).where(Task.id == task_no))).scalar_one_or_none()

    task.task_body = update_payload.task_body
    task.task_title = update_payload.task_title
    
    session.commit()
    session.refresh(task)

    return task

@router.delete("/{task_no}")
def delete_task(task_no : uuid4, session : Session = Depends(get_session)):
    task = (session.execute(select(Task).where(Task.id == task_no))).scalar_one_or_none()

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {task_no} Not found"
        )

    session.delete(task)
    session.commit()

    return {"msg": f"Task {task_no} successfully Deleted!"}