from fastapi import APIRouter

from schemas.hotel_booking import HotelBooking
from pre_processing import pre_processing as prepro
from ml_models.classifier import Classifier

router = APIRouter()

@router.post("/predict/")
def predict(data: HotelBooking):
    cls = Classifier()
    cls.load_model()

    input_data = prepro.pre_process(data.dict())
    prob = cls.model.predict_proba(input_data)[0][1]

    return{
        'probability': prob,
        'features': input_data.iloc[0].to_dict()
    }