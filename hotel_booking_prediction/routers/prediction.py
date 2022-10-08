from fastapi import APIRouter

from schemas.hotel_booking import HotelBooking

router = APIRouter()

@router.post("/predict/")
def predict(request: HotelBooking):
    return request