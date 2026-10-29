from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/test")
def get_user():
    return {"msg":"User routes is running!"}
