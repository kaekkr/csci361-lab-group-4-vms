from fastapi import FastAPI

from src.auth.router import router as auth_router
from src.user.router import router as user_router
import src.database.models as models
from src.database.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(user_router, prefix="/user", tags=["user"])