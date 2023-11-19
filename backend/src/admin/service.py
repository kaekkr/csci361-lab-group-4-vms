"""User Service module."""

from src.database.models import Admin
from src.database.repositories import AdminRepository
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from typing import Annotated

from src.database.schemas import TokenData
from src.config import SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class AdminService:

    def __init__(self, admin_repository: AdminRepository) -> None:
        self._repository: AdminRepository = admin_repository

    def get_user_by_email(self, email: str) -> Admin:
        return self._repository.get_by_email(email)

    async def get_current_user(self, token: Annotated[str, Depends(oauth2_scheme)]):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            token_data = TokenData(username=username)
        except JWTError:
            raise credentials_exception
        user = self.get_user_by_email(token_data.username)
        if user is None:
            raise credentials_exception
        return user

    async def get_current_active_user(
        current_user: Annotated[Admin, Depends(get_current_user)]
    ):
        if current_user.disabled:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user
