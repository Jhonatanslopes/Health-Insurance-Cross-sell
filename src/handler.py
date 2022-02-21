import pickle
import pandas as pd
from class_.CarInsurance import CarInsurance
from flask import Flask, request, Response
import os
import xgboost as xgb

# loading model
model = pickle.load(open('model/xgboost.pkl', 'rb'))

# Initialize API
app = Flask(__name__)


@app.route('/carInsurance/predict', methods=['POST'])
def carInsurance_predict():

    test_json = request.get_json()

    if test_json:  # There is data
        if isinstance(test_json, dict):  # unique exemple
            test_raw = pd.DataFrame(test_json, index=[0])

        else:  # multiple example
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())

        # Instantiate Class
        pipeline = CarInsurance()

        # data cleaning
        df1 = pipeline.cleaning(test_raw)
        print('cleaning ok')

        # feature engineering
        df2 = pipeline.feature_engineering(df1)
        print('feature engineering ok')

        # data preparation
        df3 = pipeline.preparation(df2)
        print('preparation ok')

        # prediction
        df_response = pipeline.get_prediction(
            model=model, original_data=df1, test_data=df3)
        print("prediction ok")

        return df_response

    else:
        return Response('{}', status=200, minetype='application/json')


if __name__ == '__main__':
    porta = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=porta)
