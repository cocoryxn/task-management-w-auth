from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.modules.users.schema import CreateUser, CreatedUserResponse
from app.core.security import (hash_password, verify_password)
from app.modules.users.models import User

from app.database.session import get_session

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=CreatedUserResponse, status_code=status.HTTP_201_CREATED)
def register(payload : CreateUser, session : Session = Depends(get_session)):
    existing =  (session.execute(select(User).where(User.email == payload.email))).scalar_one_or_none()

    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User is already exist"
        )

    user_ = User(
        email=payload.email,
        username=payload.username,
        password=hash_password(payload.hash_password)
    )

    session.add(user_)
    session.commit()

    return {"msg":"Succesfully Registered!"}
    