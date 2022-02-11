import pickle
import pandas as pd
from class_.CarInsurance import CarInsurance
from flask import Flask, request, Response

# loading model
path = 'C:/Users/Jhonatans/projects/ML/Classification/Health-Insurance-Cross-Sell/'
model = pickle.load(open(path + 'src/model/xgboost.pkl', 'rb'))

# Initialize API
app = Flask(__name__)

@app.route('/carInsurance/predict', methods=['POST'])
def carInsurance_predict():
    
    test_json = request.get_json()
    
    if test_json: # There is data
        if isinstance(test_json, dict): # unique exemple
            test_raw = pd.DataFrame(test_json, index=[0])
            
        else: # multiple example
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())
            
        # Instantiate Class
        pipeline = CarInsurance()
        
        # data cleaning
        df1 = pipeline.cleaning(test_raw)
        
        # feature engineering
        df2 = pipeline.feature_engineering(df1)
        
        # data preparation
        df3 = pipeline.preparation(df2)
        
        # prediction
        df_response = pipeline.get_prediction(model, test_raw, df3)
        
        return df_response
    
    else:
        return Response('{}', status=200, mimetype='application/json')
    
if __name__ =='__main__':
    app.run('0.0.0.0', debug=True)