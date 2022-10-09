import pandas as pd

from hotel_booking_prediction.pre_processing import cat_features as cat
from hotel_booking_prediction.pre_processing import num_features as num

def get_cat_features() -> list:
    return ['hotel',
            'arrival_date_month',
            'meal',
            'market_segment',
            'distribution_channel',
            'reserved_room_type',
            'deposit_type',
            'customer_type',
            'reservation_status_date']

def get_num_features() -> list:
    return ['lead_time',
            'arrival_date_week_number',
            'arrival_date_day_of_month',
            'stays_in_weekend_nights',
            'stays_in_week_nights',
            'adults',
            'children',
            'babies',
            'is_repeated_guest',
            'previous_cancellations',
            'previous_bookings_not_canceled',
            'agent',
            'company',
            'adr',
            'required_car_parking_spaces',
            'total_of_special_requests']

def pre_process(data: dict) -> pd.DataFrame:
    df = pd.DataFrame.from_dict(
        data, orient='index').T

    cat_df = cat.apply_cat_transformations(df[get_cat_features()])
    num_df = num.normalize_features(df[get_num_features()])

    return pd.concat([cat_df, num_df], axis = 1)