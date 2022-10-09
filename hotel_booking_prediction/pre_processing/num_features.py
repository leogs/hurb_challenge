import numpy as np
import pandas as pd


def normalize_features(df: pd.DataFrame) -> pd.DataFrame:
    df['lead_time'] = np.log(pd.to_numeric(df['lead_time']) + 1)
    df['arrival_date_week_number'] = np.log(pd.to_numeric(df['arrival_date_week_number']) + 1)
    df['arrival_date_day_of_month'] = np.log(pd.to_numeric(df['arrival_date_day_of_month']) + 1)
    df['agent'] = np.log(pd.to_numeric(df['agent']) + 1)
    df['company'] = np.log(pd.to_numeric(df['company']) + 1)
    df['adr'] = np.log(pd.to_numeric(df['adr']) + 1)

    return df