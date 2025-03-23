from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.model_tranier import ModelTrainer

if __name__ == "__main__":
    logging.info("The Exception has started")

    try:
        #data_ingestion_config = DataIngestionConfig()
        # data_ingestion = DataIngestion()
        # data_ingestion.initiate_data_ingestion()

        obj = DataIngestion()
        train_data, test_data = obj.initiate_data_ingestion()

        data_transformation = DataTransformation()
        train_arr, test_arr = data_transformation.initiate_data_transformation(train_data, test_data)

        model_trainer = ModelTrainer()
        accuracy = model_trainer.initiate_model_trainer(train_arr, test_arr)
        print(f"Best model accuracy: {accuracy}")

        
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
