from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.mlproject.pipelines.prediction_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = CustomData(
            age=int(request.form.get('age')),
            anaemia=int(request.form.get('anaemia')),
            creatinine_phosphokinase=int(request.form.get('creatinine_phosphokinase')),
            diabetes=int(request.form.get('diabetes')),
            ejection_fraction=int(request.form.get('ejection_fraction')),
            high_blood_pressure=int(request.form.get('high_blood_pressure')),
            platelets=float(request.form.get('platelets')),
            serum_creatinine=float(request.form.get('serum_creatinine')),
            serum_sodium=int(request.form.get('serum_sodium')),
            sex=int(request.form.get('sex')),
            smoking=int(request.form.get('smoking')),
            time=int(request.form.get('time'))
        )

        pred_df = data.get_data_as_data_frame()
        predict_pipeline = PredictPipeline()
        prediction = predict_pipeline.predict(pred_df)

        return render_template('index.html', prediction=prediction[0])

if __name__ == "__main__":
    app.run(host="0.0.0.0")