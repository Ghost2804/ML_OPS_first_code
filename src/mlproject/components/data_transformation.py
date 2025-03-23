# import sys
# from dataclasses import dataclass

# import numpy as np 
# import pandas as pd
# from sklearn.compose import ColumnTransformer
# from sklearn.impute import SimpleImputer
# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import OneHotEncoder,StandardScaler

# from src.mlproject.exception import CustomException
# from src.mlproject.logger import logging
# import os

# from src.mlproject.utils import save_object

# @dataclass
# class DataTransformationConfig:
#     preprocessor_obj_file_path=os.path.join('artifacts',"proprocessor.pkl")


# class DataTransformation:

#     def initiate_data_transformation(self,train_path,test_path):

#             try:
                
#                 train_df = pd.read_csv(train_path)
#                 test_df = pd.read_csv(test_path)

#                 logging.info("Read train and test data completed")

#                 target_column_name = "DEATH_EVENT"

#                 # Drop DEATH_EVENT from train and convert to array
#                 input_feature_train_arr = train_df.drop(columns=[target_column_name], axis=1).to_numpy()
#                 # Convert test to array as is
#                 input_feature_test_arr = test_df.to_numpy()

#                 # Since DEATH_EVENT is dropped from train, we can keep it simple
#                 train_arr = input_feature_train_arr
#                 test_arr = input_feature_test_arr

#                 logging.info("Converted dataframes to arrays successfully")

#                 return (
#                     train_arr,
#                     test_arr,
#                 )

#             except Exception as e:
#                 raise CustomException(e,sys)


# src/mlproject/components/data_transformation.py
import sys
from dataclasses import dataclass
import numpy as np 
import pandas as pd
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import os

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Read train and test data completed")

            target_column_name = "DEATH_EVENT"

            # Ensure target column is the last column in both train and test
            columns = [col for col in train_df.columns if col != target_column_name] + [target_column_name]
            train_df = train_df[columns]
            test_df = test_df[columns]

            # Convert to numpy arrays
            train_arr = train_df.to_numpy()
            test_arr = test_df.to_numpy()

            logging.info("Converted dataframes to arrays successfully")

            return train_arr, test_arr

        except Exception as e:
            raise CustomException(e, sys)