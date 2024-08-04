
import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from src.utils.exception import CustomException
from src.utils.logger import logger
'''
Data Ingestion class takes input csv files, pre-process and clean the data, split data and save into train and test 
'''


class DataIngestion:

    def ingest_data(self):
        logger.info("Beginning Data Ingestion")
        try:
            cwd = os.getcwd()
            file_path = os.path.join(cwd,"data","csv", "bmi.csv")
            
            ## read CSV File
            df = pd.read_csv(file_path)
            logger.info("Reading data set into data frame")
            artifact_path=os.path.join(cwd,"artifacts")
            
            os.makedirs(artifact_path,exist_ok=True)

            train_set, test_set = train_test_split(df,test_size=0.4,random_state=88)

            ## writing csv file
            train_file_path = os.path.join(artifact_path,"train.csv")
            test_file_path = os.path.join(artifact_path,"test.csv")

            train_set.to_csv(train_file_path,index=False,header=True)
            test_set.to_csv(test_file_path,index=False,header=True)

            logger.info("Written test and training files")

            return (train_file_path,test_file_path)
            

        except Exception as e:
            CustomException(e.__str__,e.__traceback__)    







if __name__ == "__main__":
    dataIngestion = DataIngestion()
    train_file_path,test_file_path = dataIngestion.ingest_data()
    print(train_file_path,test_file_path)
