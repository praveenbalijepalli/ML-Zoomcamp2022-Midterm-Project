### Predict script ###


# Import Libraries
import numpy as np
import pandas as pd

import pickle

# Import ML library and its modules
import sklearn
from sklearn.ensemble import RandomForestClassifier

# Data Engineering
from sklearn.feature_extraction import DictVectorizer
 
# Import custom preprocessing utility functions
from preprocessing import  data_extractor, remove_url_ip_content_features 

# Import Flask and its utilities
from flask import Flask
from flask import request 
from flask import jsonify

# Load DictVectorizer and Model
model_file = 'model.bin'
                        
with open(model_file,'rb') as f_in:         
    selected_features, dv, model = pickle.load(f_in) # Loading the selected_features, dictvectorizer and the trained model objects to a variable
        

app = Flask('classify')

@app.route("/predict", methods=["POST"])
def predict():
    
    data = request.get_json()
    
    df = pd.DataFrame(data, index=[0])
 
    # Preprocess the dataframe
    df = data_extractor(df)
    df = remove_url_ip_content_features(df)
    
    # DictVectorize the dataframe
    df_dict = df.to_dict(orient='records')
    df_dv = dv.transform(df_dict)
    df_dv_cols = list(dv.get_feature_names_out())
    X = pd.DataFrame(data=df_dv, columns=df_dv_cols)
    
    prediction = model.predict(X[selected_features]).item(0)  # Return a scalar instead of an array
    
    if prediction==1:
        result = { "label": "Bad" }
    else:
        result = { "label": "Good" }   
 
 
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',   port=9696)