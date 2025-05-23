import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split

from src.mlproject.utils import read_sql_data

from src.mlproject.components.data_transformation import DataTransformation


from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts', 'train.csv')
    test_data_path:str = os.path.join('artifacts', 'test.csv')
    raw_data_path:str = os.path.join('artifacts', 'raw.csv')


class DataIngestion:    
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):

        try:
            df = pd.read_csv(r'C:\Users\AnayJoshi28\Desktop\Projects\Data Scientist Projects\ML_OPS\NEW_project_1\notebook\data\raw.csv')
            logging.info("Reading from raw dataset")

            if df is None or df.empty:
                logging.error("Error: read_sql_data() returned None or an empty DataFrame.")
                raise ValueError("Data could not be fetched from SQL.")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index = False, header = True)
            train_set,test_set = train_test_split(df,test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index = False, header = True)
            test_set.to_csv(self.ingestion_config.test_data_path,index = False, header = True)

            logging.info("Data ingestion is complete")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)
        

if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_trainformation = DataTransformation()
    data_trainformation.initiateinitiate_data_transformation(train_data,test_data)
    