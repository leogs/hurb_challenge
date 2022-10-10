import os
import json
from typing import Tuple

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, confusion_matrix, classification_report
from catboost import CatBoostClassifier
import mlflow
import mlflow.catboost as ml_cat
from minio import Minio
from minio.error import InvalidResponseError

from pre_processing import cat_features as cat_feat
from pre_processing import num_features as num
from pre_processing import pre_processing as prepro
from config import settings


def read_file(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

def data_cleansing(df: pd.DataFrame) -> pd.DataFrame:
    df.fillna(0, inplace = True)

    return df

def data_target_split(
    df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:

    y = df['is_canceled']
    df.drop('is_canceled', axis = 1, inplace = True)

    return df, y

def encode_features(df: pd.DataFrame) -> pd.DataFrame:
    cat_df = cat_feat.apply_cat_transformations(
        df[prepro.get_cat_features()])

    num_df = num.normalize_features(
        df[prepro.get_num_features()])
    
    num_df['adr'] = num_df['adr'].fillna(
        value = df['adr'].mean())

    return pd.concat([cat_df, num_df], axis = 1)

def get_minio_bucket() -> None:
    minioClient = Minio(os.environ['MLFLOW_S3_ENDPOINT_URL'].split('//')[1],
                  access_key=os.environ['AWS_ACCESS_KEY_ID'],
                  secret_key=os.environ['AWS_SECRET_ACCESS_KEY'],
                  secure=False)
    if minioClient.bucket_exists("mlflow"):
        print("mlflow exists")
    else:
        try:
            minioClient.make_bucket('mlflow')
        except InvalidResponseError as err:
            print(err)

    policy = {"Version":"2012-10-17",
        "Statement":[
            {
            "Sid":"",
            "Effect":"Allow",
            "Principal":{"AWS":"*"},
            "Action":"s3:GetBucketLocation",
            "Resource":"arn:aws:s3:::mlflow"
            },
            {
            "Sid":"",
            "Effect":"Allow",
            "Principal":{"AWS":"*"},
            "Action":"s3:ListBucket",
            "Resource":"arn:aws:s3:::mlflow"
            },
            {
            "Sid":"",
            "Effect":"Allow",
            "Principal":{"AWS":"*"},
            "Action":"s3:GetObject",
            "Resource":"arn:aws:s3:::mlflow/*"
            },
            {
            "Sid":"",
            "Effect":"Allow",
            "Principal":{"AWS":"*"},
            "Action":"s3:PutObject",
            "Resource":"arn:aws:s3:::mlflow/*"
            }

        ]}
    
    minioClient.set_bucket_policy('mlflow', json.dumps(policy))

def train_and_evaluate():
    os.environ['MLFLOW_S3_ENDPOINT_URL'] = settings.mlflow_s3_endpoint_url
    os.environ['AWS_ACCESS_KEY_ID'] = settings.aws_access_key_id
    os.environ['AWS_SECRET_ACCESS_KEY'] = settings.aws_secret_access_key

    mlflow.set_tracking_uri('http://mlflow-service:5000')

    get_minio_bucket()

    df = read_file(settings.data_url)
    df = data_cleansing(df)

    X, y = data_target_split(df)

    X = encode_features(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size = 0.30, random_state=16)

    with mlflow.start_run():
        cat = CatBoostClassifier(iterations=100)
        cat.fit(X_train, y_train)

        y_pred_cat = cat.predict(X_test)

        acc_cat = accuracy_score(y_test, y_pred_cat)
        f1 = f1_score(y_test, y_pred_cat)
        auc = roc_auc_score(y_test, y_pred_cat)

        mlflow.log_param('accuracy', acc_cat)
        mlflow.log_param('f1', f1)
        mlflow.log_param('roc_auc', auc)

        model_name = 'hotel-booking-prediction-model'

        ml_cat.save_model(cat, 'catboost_model')

        ml_cat.log_model(cb_model = cat,
                        artifact_path = 'catboost_model',
                        registered_model_name = model_name)



        conf = confusion_matrix(y_test, y_pred_cat)
        clf_report = classification_report(y_test, y_pred_cat)
    
    return {'model_name': model_name,
            'model_accuracy': acc_cat}