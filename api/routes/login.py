import os
from datetime import timedelta
from typing import Annotated
from dotenv import load_dotenv
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status
from starlette.exceptions import HTTPException

from api.dependencies import authenticate_user, create_access_token
from api.models.structural.TokenModels import Token

router = APIRouter(
    prefix="/login",
    tags=["login"]
)

load_dotenv()

ACCESS_TOKEN_EXPIRE_MINUTES = float(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


@router.post("/", response_model=Token, summary="Login one user")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.handler}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")