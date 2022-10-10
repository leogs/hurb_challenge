from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str
    ml_model_serialized: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"

settings = Settings()