from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str
    ml_model_serialized: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    mlflow_s3_endpoint_url: str
    aws_access_key_id: str
    aws_secret_access_key: str
    data_url: str


    class Config:
        env_file = ".env"

settings = Settings()