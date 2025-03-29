import sys
import os
import pandas as pd
from src.mlproject.exception import CustomException
from src.mlproject.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            print("Before Loading Model")
            model = load_object(file_path=model_path)
            print("After Loading Model")
            preds = model.predict(features)
            return preds
        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self, age: int, anaemia: int, creatinine_phosphokinase: int, diabetes: int,
                 ejection_fraction: int, high_blood_pressure: int, platelets: float,
                 serum_creatinine: float, serum_sodium: int, sex: int, smoking: int, time: int):
        
        self.age = age
        self.anaemia = anaemia
        self.creatinine_phosphokinase = creatinine_phosphokinase
        self.diabetes = diabetes
        self.ejection_fraction = ejection_fraction
        self.high_blood_pressure = high_blood_pressure
        self.platelets = platelets
        self.serum_creatinine = serum_creatinine
        self.serum_sodium = serum_sodium
        self.sex = sex
        self.smoking = smoking
        self.time = time

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "age": [self.age],
                "anaemia": [self.anaemia],
                "creatinine_phosphokinase": [self.creatinine_phosphokinase],
                "diabetes": [self.diabetes],
                "ejection_fraction": [self.ejection_fraction],
                "high_blood_pressure": [self.high_blood_pressure],
                "platelets": [self.platelets],
                "serum_creatinine": [self.serum_creatinine],
                "serum_sodium": [self.serum_sodium],
                "sex": [self.sex],
                "smoking": [self.smoking],
                "time": [self.time],
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e, sys)

