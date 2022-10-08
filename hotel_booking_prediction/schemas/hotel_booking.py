from pydantic import BaseModel

class HotelBooking(BaseModel):
    hotel: str
    arrival_date_month: str
    meal: str
    market_segment: str
    distribution_channel: str
    reserved_room_type: str
    deposit_type: str
    customer_type: str
    reservation_status_date: str
    lead_time: int
    arrival_date_week_number: int
    arrival_date_day_of_month: int
    stays_in_weekend_nights: int
    stays_in_week_nights: int
    adults: int
    children: int
    babies: int
    is_repeated_guest: int
    previous_cancellations: int
    previous_bookings_not_canceled: int
    agent: float
    company: float
    adr: float
    required_car_parking_spaces: int
    total_of_special_requests: int