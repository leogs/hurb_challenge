from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Hotel Booking Prediction API"
    ml_model_serialized: str = "./hotel_booking_prediction/artifacts/model.json"

settings = Settings()