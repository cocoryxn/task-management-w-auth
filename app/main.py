from fastapi import FastAPI

from app.modules.health.router import router as root
from app.modules.tasks.routers import router as task
from app.modules.auth.routers import router as auth

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

# auth Route
app.include_router(
    auth,
    prefix="/api/v1"
)