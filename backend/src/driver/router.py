"""Driver Endpoints module."""

from typing import Annotated
from fastapi import APIRouter, Depends, Response, status
# from dependency_injector.wiring import inject, Provide

from .service import UserService
from src.database.models import User

router = APIRouter()
