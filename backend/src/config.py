from pydantic_settings import BaseSettings 

class AppSettings(BaseSettings):
    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"
        env_prefix = "app_"

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int