import sys
import pandas as pd
from src.utils.exception import CustomException
from src.utils.logger import logger
from src.utils.utilities import save_object
from .CustomData import CustomData
from src.utils.utilities import save_object
from src.utils.utilities import load_object

class PredictionPipeline:
    def __init__(self,features):
        self.features =features

    def predict(self):
        try:
            logger.info("Begin Prediction Pipeline")
            transformer_file  = "column_transformer.pkl"
            predictor_file = "hyper_tuned_model.pkl"
            transformer_obj = load_object(transformer_file)
            predictor_obj = load_object(predictor_file)
            print(self.features)
            data = transformer_obj.transform(self.features)
            print(data)
            bmi = predictor_obj.predict(data)
            logger.info(f"Prediction came as {bmi}")
            return bmi
        
        except Exception as e:
            CustomException(e.__str__,e.__traceback__)    
