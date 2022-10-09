import pandas as pd

def get_reservation_date(df: pd.DataFrame) -> pd.DataFrame:
    df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])

    df['year'] = df['reservation_status_date'].dt.year
    df['month'] = df['reservation_status_date'].dt.month
    df['day'] = df['reservation_status_date'].dt.day

    return df.drop(
        ['reservation_status_date','arrival_date_month'],
        axis=1)

def encode_cat_features(df: pd.DataFrame) -> pd.DataFrame:
    df['hotel'] = df['hotel'].map(
        {
            'Resort Hotel' : 0,
            'City Hotel' : 1})

    df['meal'] = df['meal'].map(
        {
            'BB' : 0,
            'FB': 1,
            'HB': 2,
            'SC': 3,
            'Undefined': 4})

    df['market_segment'] = df['market_segment'].map(
        {
            'Direct': 0,
            'Corporate': 1,
            'Online TA': 2,
            'Offline TA/TO': 3,
            'Complementary': 4,
            'Groups': 5,
            'Undefined': 6,
            'Aviation': 7})

    df['distribution_channel'] = df['distribution_channel'].map(
        {
            'Direct': 0,
            'Corporate': 1,
            'TA/TO': 2,
            'Undefined': 3,
            'GDS': 4})

    df['reserved_room_type'] = df['reserved_room_type'].map(
        {
            'C': 0,
            'A': 1,
            'D': 2,
            'E': 3,
            'G': 4,
            'F': 5,
            'H': 6,
            'L': 7,
            'B': 8})

    df['deposit_type'] = df['deposit_type'].map(
        {
            'No Deposit': 0,
            'Refundable': 1,
            'Non Refund': 3})

    df['customer_type'] = df['customer_type'].map(
        {
            'Transient': 0,
            'Contract': 1,
            'Transient-Party': 2,
            'Group': 3})

    df['year'] = df['year'].map(
        {
            2015: 0,
            2014: 1,
            2016: 2,
            2017: 3})
    
    return df

def apply_cat_transformations(df: pd.DataFrame) -> pd.DataFrame:
    return df.pipe(
            get_reservation_date
            ).pipe(encode_cat_features)