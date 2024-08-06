from src.utils.exception import CustomException
import pandas as pd

class CustomData:
    def __init__(self,height:int,weight:int,gender:str):
        self.height = height
        self.weight = weight
        self.gender = gender

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Height": [self.height],
                "Weight": [self.weight],
                "Gender": [self.gender]
                
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e.__str__, e.__traceback__)    