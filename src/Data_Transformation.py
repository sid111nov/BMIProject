import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from src.utils.exception import CustomException
from src.utils.logger import logger
from src.utils.utilities import save_object

## Data transformation reads the csv files train and test and 

## Clean and preprocess the data set applies imputation and transformation and save it into dataset
class DataTransformation:
    def __init__(self,train_file_path,test_file_path):
        self.train_file_path = train_file_path
        self.test_file_path = test_file_path

    def data_preprocessing(self):
        try:
            logger.info("Starting Preprocessing")
            df_train,df_test = self.dataFrameExtract()
            
            cat_columns = df_train.select_dtypes(include=['object']).columns
            numeric_columns = df_train.select_dtypes(exclude=['object']).columns

            numeric_columns = numeric_columns.drop('Index')

            num_transformer = StandardScaler()
            cat_transformer = OneHotEncoder()

            col_transformer = ColumnTransformer(
            transformers = [
                        ('num_transform',num_transformer,numeric_columns),
                        ('cat_transform',cat_transformer,cat_columns)
            ]
            )

            return col_transformer


            
        except Exception as e:
            CustomException(e.__str__,e.__traceback__)

    def dataFrameExtract(self):
        train_path = self.train_file_path
        test_path = self.test_file_path

        df_train = pd.read_csv(train_path)
        df_test = pd.read_csv(test_path)
        
        return df_train,df_test

    def data_transformation(self):
        logger.info("Beginning Data Transformation")
        
        try:
            print(self.test_file_path,self.train_file_path)
            df_train,df_test = self.dataFrameExtract()
            col_transformer  = self.data_preprocessing()
            
            Y_train = df_train['Index']
            X_train=df_train.drop(columns='Index',axis=1)

            Y_test = df_test['Index']
            X_test = df_test.drop(columns='Index',axis=1)

            X_train = col_transformer.fit_transform(X_train)
            X_test = col_transformer.transform(X_test)
            
            train_array = np.c_[
                X_train, np.array(Y_train)
            ]

            test_array = np.c_[
                X_test, np.array(Y_test)
            ]

            file_loc = save_object(col_transformer,'column_transformer')

            return(
                train_array,
                test_array,
                file_loc
            )



        except Exception as e:
            CustomException(e.__str__,e.__traceback__)        

if __name__ == "__main__":
    cwd = os.getcwd()
    artifact_path=os.path.join(cwd,"artifacts")
    train_file_path = os.path.join(artifact_path,"train.csv")
    test_file_path = os.path.join(artifact_path,"test.csv")
    
    data_Trasformation = DataTransformation(train_file_path,test_file_path)
    
    train_arr,test_arr, preprocessor = data_Trasformation.data_transformation()
    