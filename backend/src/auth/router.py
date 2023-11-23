"""Auth Endpoints module."""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from dependency_injector.wiring import inject, Provide

from src.auth.service import AuthService
from src.config import ACCESS_TOKEN_EXPIRE_MINUTES
from src.containers import Container

router = APIRouter()


@router.post("/login/")
@inject
def login_for_access_token(
    user_type: str, 
    auth_service: AuthService = Depends(Provide[Container.auth_service]), 
    form_data: OAuth2PasswordRequestForm = Depends()
    ):
    user = auth_service.authenticate_user(
        user_type, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth_service.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer", "user": user}