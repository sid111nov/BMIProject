import pandas as pd
import numpy as np
import os
from src.utils.exception import CustomException
from src.utils.logger import logger
from src.utils.utilities import save_object
from src.utils.utilities import load_object
from src.models.Models import Models
from sklearn.model_selection import GridSearchCV

class Model_Trainer:
    def __init__(self,train_arr,test_arr, preprocessor_fileLoc):
        self.preprocessor = preprocessor_fileLoc
        X_train,Y_train,X_test,Y_test=(
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )
        self.X_train = X_train
        self.Y_train = Y_train
        self.X_test = X_test
        self.Y_test = Y_test
        

    def train_models(self):
        try:

            logger.info("Model Training begins here")
            models = Models()
            models_dict = models.get_Model_Dict()

            model_results = {
    
            }

            for name,model in models_dict.items():
                model.fit(self.X_train,self.Y_train)
                prediction = model.predict(self.X_test)
                prediction = np.clip(np.round(prediction).astype(int),a_min=0,a_max=5)

                score = models.get_Scores(self.Y_test,prediction)
                logger.info(f"name: {name}, mse: {score[0]}, r2: {score[1]}, mape: {score[2]}")
                
                model_results[name]={'scores': score, 'model': model}


            best_model = min(model_results, key=lambda x: model_results[x]["scores"][0])

            logger.info(f'Best model: {best_model}')
            logger.info(f'Best model results: {model_results[best_model]}')

            print(f'Best model results: {model_results[best_model]}')

            best_model_found = model_results[best_model]["model"]
            save_object(best_model_found,"prediction_model")

            ## Hyper parameter tuning it further 

            hyper = models.get_Hyper_Params()
           
            gridsearchCV = GridSearchCV(models_dict[best_model],hyper[best_model],cv=5)
            gridsearchCV.fit(self.X_train,self.Y_train)
            
            print("Best hyperparameters:", gridsearchCV.best_params_)
            print("Best score:", gridsearchCV.best_score_)

            best_model = gridsearchCV.best_estimator_
            predictions = best_model.predict(self.X_test)

            
            print(f'hyper tuned model results: {models.get_Scores(self.Y_test,predictions)}')
            save_object(best_model_found,"hyper_tuned_model")




        except Exception as e:
            CustomException(e.__str__,e.__traceback__)        



        
