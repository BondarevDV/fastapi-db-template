from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from models import Token, Login
from repositories.users import UserRepository
from .depends import get_user_repository
from core.security import verify_passwd, create_access_token

router = APIRouter()

@router.post("/", response_model=Token)
async def login(login: Login, users: UserRepository = Depends(get_user_repository)):
    user = await users.get_by_email(email=login.email)
    if user is None or not verify_passwd(login.passwd, user.h_passwd):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    return Token(
        access_token=create_access_token({"sub": user.email}),
        token_type="Bearer"
    )
        