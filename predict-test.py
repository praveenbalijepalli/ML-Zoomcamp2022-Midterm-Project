
#Import libraries
import pandas as pd
import requests
import json

 
test = pd.read_csv("sampled_webpages_classification_test_data.csv")
 
url = "http://127.0.0.1:9696/predict"
 
    
### Test input 1
test_data1 = test.sample(1, random_state=100)  
print("Test input data 1 with label to verify the predicted output: \n", test_data1)
print("\n\n")

test_data1.drop("label", axis=1, inplace=True) # Dropping label column because it should be the predicted output
dict_test_data1 = json.loads(test_data1.to_json(orient='records', lines=True))

response1 = requests.post(url, json=dict_test_data1).json()
print(response1)
print("\n\n\n")
 
### Test input 2
test_data2 = test.sample(1, random_state=362) 
print("Test input data 1 with label to verify the predicted output: \n", test_data2)
print("\n\n")

test_data2.drop("label", axis=1, inplace=True) # Dropping label column because it should be the predicted output
dict_test_data2 = json.loads(test_data2.to_json(orient='records', lines=True))
 
response2 = requests.post(url, json=dict_test_data2).json()
print(response2)
print("\n\n\n")
