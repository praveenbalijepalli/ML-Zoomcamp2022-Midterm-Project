 ## Classification of Webpages as Benign(good) or Malicious(bad) using Machine Learning
  
<pre>
Domain             : Cybersecurity, Machine Learning
Models             : RandomForestClassifier, AdaboostClassifier, XGBClassifier 
Applications       : Access Filter for Safe Browsing, Cyber Aware Browsing
</pre>

 
 ## Problem Statement 
 
 As the world grows ever more reliant on the internet for information, transactions and entertainment, there is also a challenging task to ensure the online security of unsuspecting users from the ever rising threats due to websites which can be unsuspectingly malicious. These websites can be used for a variety of tricks by the hackers to trap users without their knowledge. These can be anything from phishing, malware installation, ransomware deployment and stealing financial information of the user while they unsuspecting browse the website or perform transaction on a malicious webpage. The general idea of this project is to identify the methods malicious websites use to fool the users to help inform our classification of webpages as good or bad so that the users are made aware of the nature of the websites they're visiting. Additionally, the model developed from the project can also used as an access filter for safe browsing. For example, URL redirection, maliciously using iframes, long obfuscating javascript code, using javascript eval() and find() maliciously and so on. So, in order to do this, dataset I have considered to train the classifier model is from the work of [Singh, AK (2020), “Dataset of Malicious and Benign Webpages”, Mendeley Data, V2, doi: 10.17632/gdx3pkwp47.2](https://data.mendeley.com/datasets/gdx3pkwp47/2). <br>
 
I downloaded and extracted the contents of the zip file from the link shown and downsampled the data from "Webpages_Classification_train_data.csv" and "Webpages_Classification_test_data.csv" while maintaining the proportion of the labels as closely as possible to get a more manageable dataset for training and testing. The downsampled files are shared in this  repository.<br>
 
 The dataset is however imbalanced towards 'good' labels which almost account for close to 97.5% of the data.
- [Train Dataset](https://github.com/praveenbalijepalli/zoomcamp2022-midterm-project/blob/main/sampled_webpages_classification_train_data.csv)
- [Test Dataset](https://github.com/praveenbalijepalli/zoomcamp2022-midterm-project/blob/main/sampled_webpages_classification_test_data.csv)  
      
## Dataset Description:

The dataset contains extracted attributes from websites that can be used for Classification of webpages as bad(malicious) or good(benign). It includes, url, raw page content with javascript code which can be used to extract more features. In addition to some more features such as ip addresses, geographic location, who is information completeness have also be considered. Singh, AK mentions that the data was collected by crawling the Internet using MalCrawler. Additionally the labels were verified by them using the Google Safe Browsing API. They selected attributes based on the relevance. The details of dataset attributes are the following: 

<pre>
'url'             - The URL of the webpage.
'ip_add'          - IP Address of the webpage.
'geo_loc'         - The geographic location where the webpage is hosted.
'url_len'         - The length of URL.
'js_len'          - Length of JavaScript code on the webpage.
'js_obf_len'      - Length of obfuscated JavaScript code.
'tld'             - The Top Level Domain of the webpage.
'who_is'          - Whether the WHO IS domain information is compete or not.
'https'           - Whether the site uses https or http.
'content'         - The raw webpage content including JavaScript code.
'label'           - The class label for benign or malicious webpage. :
 </pre>   
      

## Exploratory Data Analysis
Exploratory Data Analysis was performed on the train dataset to understand the relationship between label and features of the dataset after cleaning the dataset. The analysis was structured based on the whether the features were numeric or categorical and also the their relationship with the cleaned target(label) column('bad:1 and 'good:0). Further univariate, bivariate and correlation analysis was done followed by data extraction, feature selection, balancing imbalanced dataset and hypertuning and saving the model. 
- [Notebook.ipynb](https://github.com/praveenbalijepalli/zoomcamp2022-midterm-project/blob/main/Notebook%20.ipynb)

## Training  
Multiple models were considered for training and some of them were selected for hypertuning their performance. And the best performing model was considered for the final prediction. Feature selection was done based on Model Based Feature Selection approach and the model used for feature selection was RandomForestClassifier(n=100)
 
## Train and Predict Scripts  
Since the model development involved data cleaning, data extraction, feature selection, balancing imbalanced dataset and hypertuning, a preprocessing utlity function python file was created which was used by in both train and predict scripts.The link to preprocessing, train and predict scripts are below:

- [preprocessing.py](https://github.com/praveenbalijepalli/zoomcamp2022-midterm-project/blob/main/preprocessing.py)
- [train.py](https://github.com/praveenbalijepalli/zoomcamp2022-midterm-project/blob/main/train.py)
- [predict.py](https://github.com/praveenbalijepalli/zoomcamp2022-midterm-project/blob/main/predict.py)

 
## Model as a web service 
 
 Put your model into a web service and deploy it locally with Docker
    Bonus points for deploying the service to the cloud
  
####  Sample Input: 
####  Sample Output: 

 
#### Tools / Libraries
<pre>
Language                : Python
Virtual Environment     : Anaconda
IDEs                    : Jupyter Notebook, Jupyterlab, Visual Studio Code
Libraries               : Numpy, Pandas, Matplotlib, Seaborn, Xgboost, Scikit-learn, Imbalanced-learn
Web Service             : Flask, Waitress
Container               : Docker
</pre>
 
