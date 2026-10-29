from fastapi import FastAPI

from app.modules.health.router import router as root
from app.modules.tasks.routers import router as task
from app.modules.users.routers import router as user

app = FastAPI()


#  root Router
app.include_router(
    root,
    prefix="/api/v1",
)

# task Route
app.include_router(
    task,
    prefix="/api/v1"
)

# user Route
app.include_router(
    user,
    prefix="/api/v1"
)