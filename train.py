### Train script ###


# Import Libraries
import numpy as np
import pandas as pd

import pickle 

# Import ML library and its modules
import sklearn
 
## Import train_test_split, cross_val_score, KFold - Validation and GridSearchCV  
from sklearn.model_selection import  train_test_split, cross_val_score, GridSearchCV, KFold 

# Import Classifiers - Modelling
from sklearn.ensemble import RandomForestClassifier 
    
# Data Engineering
from sklearn.feature_extraction import DictVectorizer
 
# Import custom preprocessing utility functions
from preprocessing import (load_data, clean_data, data_extractor, remove_url_ip_content_features, df_dictvectorizer, 
                           train_validation_split, train_balance_resampling, feature_selection)

# Setting options
import warnings
warnings.filterwarnings("ignore")
pd.set_option('display.max_columns', None)

 

## Train Parameters
feature_importance_threshold = 0.005
test_size = 0.2
random_state = 100
path="./"
file_name="sampled_webpages_classification_train_data.csv"




## Train the model
def training(path, file_name):
    
    df = load_data(path, file_name)
    df = clean_data(df)
    df = data_extractor(df)
    df = remove_url_ip_content_features(df)
    dv, df = df_dictvectorizer(df)
    
    x_train, x_val, y_train, y_val = train_validation_split(df,test_size = test_size, random_state = random_state)
    
    x_train_SMOTE, y_train_SMOTE = train_balance_resampling(x_train, y_train)

    
    x_train_SMOTE, y_train_SMOTE, imp_cols = feature_selection(x_train_SMOTE, y_train_SMOTE,
                                                               feature_importance_threshold=feature_importance_threshold)
   
    # Hyperparameter tuning with GridSearchCV i.e. includes K-Fold crossvalidation
    param_grid = {'criterion':['gini','entropy','cross_entropy'],
                  'max_depth':[2, 3, 4, 5, 6, 7, 8, 9],
                  'random_state':[100],
                  'n_estimators':[200,400,600],
                  'n_jobs':[-1], 
                  'random_state':[100],
                  'verbose': [0]
                 }

    RF_grid = GridSearchCV(RandomForestClassifier(), param_grid=param_grid, cv = 5, scoring='balanced_accuracy', verbose=1)

    RF_grid.fit(x_train_SMOTE, y_train_SMOTE)
    
    model = RF_grid.best_estimator_
 
    return imp_cols, dv, model # Output of training is a important columns list, dictvectorizer and model object




selected_features, dv, model = training(path, file_name) # Assigning the selected_features, dictvectorizer and the trained model objects to a variable


## Save the model
model_file = "model.bin"

with open(model_file,'wb') as f_out:
    pickle.dump((selected_features, dv, model), f_out)# Saving the selected_features, dictvectorizer and the trained model objects to a file

