from pydantic import BaseModel, validator

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

    @validator('hotel')
    def hotel_name(cls, v):
        if v not in ['Resort Hotel', 'City Hotel']:
            raise ValueError('hotel name invalid')
        return v
    
    @validator('arrival_date_month')
    def valid_month(cls, v):
        months = ['July', 'August', 'September',
                'October', 'November', 'December',
                'January', 'February', 'March',
                'April', 'May', 'June']

        if v not in months:
            raise ValueError('month value invalid')
        return v
    
    @validator('meal')
    def valid_meal(cls, v):
        meals = ['BB', 'FB', 'HB', 'SC', 'Undefined']

        if v not in meals:
            raise ValueError('meal value invalid')
        return v
    
    @validator('market_segment')
    def valid_market_segment(cls, v):
        market_segments = ['Direct', 'Corporate', 'Online TA',
                'Offline TA/TO', 'Complementary',
                'Groups', 'Undefined', 'Aviation']

        if v not in market_segments:
            raise ValueError('market_segment value invalid')
        return v
    
    @validator('distribution_channel')
    def valid_distribution_channel(cls, v):
        distribution_channels = ['Direct', 'Corporate',
                                'TA/TO', 'Undefined',
                                'GDS']

        if v not in distribution_channels:
            raise ValueError('distribution_channel value invalid')
        return v
    
    @validator('reserved_room_type')
    def valid_reserved_room_type(cls, v):
        reserved_room_types = ['C', 'A', 'D', 'E',
                                'G', 'F', 'H', 'L',
                                'P', 'B']

        if v not in reserved_room_types:
            raise ValueError('reserved_room_type value invalid')
        return v
    
    @validator('deposit_type')
    def valid_deposit_type(cls, v):
        deposit_types = ['No Deposit', 'Refundable', 'Non Refund']

        if v not in deposit_types:
            raise ValueError('deposit_type value invalid')
        return v
    
    @validator('customer_type')
    def valid_customer_type(cls, v):
        customer_types = ['Transient', 'Contract',
                        'Transient-Party', 'Group']

        if v not in customer_types:
            raise ValueError('customer_type value invalid')
        return v
    
    @validator('reservation_status_date')
    def valid_reservation_status_date(cls, v):
        years = ['2014', '2015', '2016', '2017']

        if v[:4] not in years:
            raise ValueError('reservation_status_date value invalid')
        return v
    
    @validator('lead_time', 'stays_in_weekend_nights', 'stays_in_week_nights',
                'adults', 'children', 'babies', 'previous_cancellations',
                'previous_bookings_not_canceled', 'agent', 'company',
                'required_car_parking_spaces', 'total_of_special_requests')
    def positive_value(cls, v):

        if v < 0:
            raise ValueError('value must be positive or zero')
        return v
    
    @validator('arrival_date_week_number')
    def valid_week_number(cls, v):

        if v < 1 or v > 53:
            raise ValueError('arrival_date_week_number is not a valid week value')
        return v
    
    @validator('arrival_date_day_of_month')
    def valid_day_number(cls, v):

        if v < 1 or v > 31:
            raise ValueError('arrival_date_day_of_month is not a valid day value')
        return v
    
    @validator('is_repeated_guest')
    def binary_is_repeated_guest(cls, v):

        if v not in [0, 1]:
            raise ValueError('is_repeated_guest value must be 0 or 1')
        return v