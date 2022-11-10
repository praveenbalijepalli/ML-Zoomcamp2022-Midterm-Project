### Preprocessing script ###



# Import libraries for preprocessing
import numpy as np
import pandas as pd
from urllib.parse import urlparse

# Import ML library and its modules
import sklearn
from sklearn.ensemble import RandomForestClassifier

import xgboost as xgb
from xgboost.sklearn import XGBClassifier

# Library for Dealing with imbalanced datasets
import imblearn
from imblearn.over_sampling import SMOTE

## Import train_test_split, cross_val_score, KFold - Validation and GridSearchCV  
from sklearn.model_selection import  train_test_split, cross_val_score, GridSearchCV, KFold 
     
# Data Engineering
from sklearn.feature_extraction import DictVectorizer
 
# Import Metrics - Performance Evaluation
from sklearn import metrics




## Load Data
def load_data(path, file_name):
    df = pd.read_csv(path + file_name)
    return df
 
    
## Clean Data
def clean_data(df):
    df['label']=np.where(df['label']=='bad', 1, 0) # bad=1 and good=0

            ##  Useful if there is any data conversion that needs to be done by numerical or categorical features
            #   num_cols = (train.select_dtypes(exclude="object").columns.values).tolist()
            #   cat_cols = train.select_dtypes(include="object").columns.values.tolist()
    return df
 

## Extract Data from the dataframe
def data_extractor(df):
    
    # Extract url features 
    df["asperand_symbol"] = np.where(df['url'].str.contains("@"), 1, 0) # Existence of Asperand - @ symbol
    df["redirection_symbol"] = np.where(df['url'].str.removeprefix("http://").str.removeprefix("https://").str.contains("//"),
                                        1, 0) # Redirection Symbol // symbol    
    df["hyphen_symbol"] = np.where(df["url"].apply(lambda x: urlparse(x).netloc).str.contains("-"),
                                   1, 0) # Hyphen(-) Symbol
    df["multilevel_subdomains"] = np.where(df["url"].apply(lambda x: urlparse(x).netloc).str.count("\.") > 3, 1, 0)
    
    
    # Extract content features 
    df['content_len'] = df["content"].str.len()
    df["iframe"] = np.where(df["content"].str.findall("<iframe>"), 1, 0) # Presence of iframe
    df["no_of_iframes"]= df["content"].str.findall("<iframe>").apply(lambda x: len(x)) # No. of iframes 
    df["no_of_find_fn"] = df["content"].str.findall("find\(\)").apply(lambda x: len(x)) # No. of find() fns used
    df["no_of_eval_fn"] = df["content"].str.findall("eval\(\)").apply(lambda x: len(x))  # No. of eval() fns used
    
    df["content"] = df["content"].str.lower()
    df["content"] = df["content"].str.replace('\d+'," ",regex=True) # Replacing numbers with spaces 
    df['content_len'] = df['content'].str.len() 
    
    return df

 
## Remove url, ip and content features/columns from the dataframe   
def remove_url_ip_content_features(df): # As they are unique and do not help in our modeling
    df.drop(['url', 'ip_add', 'content'], axis=1, inplace =True)
    return df

 
## One-Hot encode the categorical data
def df_dictvectorizer(df):    
    
    dv = DictVectorizer(sparse=False)
    
    df_dict = df.to_dict(orient='records')
    df_dv = dv.fit_transform(df_dict)
    
    df_dv_cols = list(dv.get_feature_names_out())
    
    df = pd.DataFrame(data=df_dv, columns=df_dv_cols)
    
    return dv, df


## Split the dataset into train and validation data 
def train_validation_split(df,test_size, random_state):
    X = df.drop('label', axis=1)
    y = df['label']
    
    x_train, x_val, y_train, y_val = train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)
    
    return  x_train, x_val, y_train, y_val
 

## Balancing the dataset samples to get equal samples for both classes to train
def train_balance_resampling(x_train, y_train):
    from imblearn.over_sampling import SMOTE

    SMOTE = SMOTE()
    x_train_SMOTE, y_train_SMOTE = SMOTE.fit_resample(x_train, y_train) # fit and resample to get equal samples for both classes
    
    return  x_train_SMOTE, y_train_SMOTE
 

## Model based Feature selection using RandomForestClassifier to select feature to consider for training
def feature_selection(x_train, y_train, feature_importance_threshold):
    
    rndf = RandomForestClassifier(n_estimators=150)
    rndf.fit(x_train, y_train)
    
    importance = pd.DataFrame.from_dict({'cols':x_train.columns, 'importance': rndf.feature_importances_})
    importance = importance.sort_values(by='importance', ascending=False)
    
    imp_cols = list(importance[importance.importance >= feature_importance_threshold].cols.values)
    
    return x_train[imp_cols], y_train, imp_cols
 