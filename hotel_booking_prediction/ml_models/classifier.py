from catboost import CatBoostClassifier

from config import settings

class Classifier:
    def __init__(self):
        self.model = CatBoostClassifier()
    
    def load_model(self):
        self.model.load_model(
            settings.ml_model_serialized, format='json')