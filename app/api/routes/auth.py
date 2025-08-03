from fastapi import APIRouter, Form

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
async def login(
    username: str = Form(...),
    password: str = Form(...)
) -> dict:
    return {
        "name": "john@gmail.com",
        "token": "token"
    }
