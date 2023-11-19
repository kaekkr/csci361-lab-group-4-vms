"""Auth Service module."""

from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt

from src.admin.service import AdminService
from src.driver.service import DriverService
from src.maintaince_person.service import MaintaincePersonService
from src.fueling_person.service import FuelingPersonService
from src.config import SECRET_KEY, ALGORITHM

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:

    def __init__(
            self,
            admin_service: AdminService,
            driver_service: DriverService,
            maintaince_person_service: MaintaincePersonService,
            fueling_person_service: FuelingPersonService
    ) -> None:
        self._adminService: AdminService = admin_service
        self._driverService: DriverService = driver_service
        self._maintaincePersonService: MaintaincePersonService = maintaince_person_service
        self._fuelingPersonService: FuelingPersonService = fueling_person_service

    def verify_password(
            self,
            plain_password: str,
            hashed_password: str
    ):
        return pwd_context.verify(plain_password, hashed_password)

    def authenticate_user(self, user_type: str, email: str, password: str):
        user = None
        if user_type == "admin":
            user = self._adminService.get_admin_by_email(email)
        elif user_type == "driver":
            user = self._driverService.get_driver_by_email(email)
        elif user_type == "maintaince_person":
            user = self._maintaincePersonService.get_maintaince_person_by_email(
                email)
        elif user_type == "fueling_person":
            user = self._fuelingPersonService.get_fueling_person_by_email(
                email)

        if not user:
            return False
        if not self.verify_password(password, user.password):
            return False
        return user

    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
        return encoded_jwt
