# -*- coding: utf-8 -*-
"""
Text classification – The aim of text classification is to automatically 
classify the text documents based on pretrained categories.

Spam - ham classification using machine learning.
Applications:
    • Sentiment Analysis
    • Document classification
    • Resume shortlisting
    • Document summarization
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import string

from nltk.stem import SnowballStemmer, PorterStemmer
from nltk.corpus import stopwords
from textblob import TextBlob, Word

from sklearn.feature_extraction.text import TfidfTransformer,TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import model_selection,preprocessing, linear_model, naive_bayes
from sklearn import metrics, svm

path = os.path.abspath("Data/TextClassification/spam.csv") 

data = pd.read_csv(path, encoding='latin1')
data.columns

data =  data[['v1','v2']]
data = data.rename(columns={"v1":"Target", "v2": "Email"})

data.info()
data.head()

data['Target'].value_counts()

# Text Preprocessing and feature Engineering
"""
lower case
stop words removal
stemming
lemmatization
"""
data["Email"] = data["Email"].apply(
    lambda x: " ".join(x.lower() for x in x.split()))

stop = stopwords.words('english')

data["Email"] = data["Email"].apply(
    lambda x: " ".join(x for x in x.split() if x not in stop))

st = PorterStemmer()

data["Email"] = data["Email"].apply(
    lambda x:" ".join([st.stem(x) for x in x.split()]))

data["Email"] = data["Email"].apply(
    lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))

data.head()

# Split the data into train and test 
train_x, test_x, train_y, test_y = train_test_split(data["Email"], 
                                                    data["Target"])

# TF-IDF Generation

encoder = preprocessing.LabelEncoder()
train_y = encoder.fit_transform(train_y)
test_y = encoder.fit_transform(test_y)

tfidf_vect = TfidfVectorizer(analyzer='word', 
                             token_pattern= r'\w{1,}', 
                             max_features=5000)

tfidf_vect.fit(data["Email"])

xtrain_tfidf = tfidf_vect.transform(train_x)
xtest_tfidf = tfidf_vect.transform(test_x)

xtrain_tfidf.data

# Model Training
def train_model(classifier, 
                fv_train, 
                label, 
                fv_test, 
                is_neural_net=False):
    classifier.fit(fv_train, label)
    predicts = classifier.predict(fv_test)
    
    return metrics.accuracy_score(predicts, test_y)

# Naive Bayes
accuracy = train_model(naive_bayes.MultinomialNB(alpha= 0.2), 
                       xtrain_tfidf,
                       train_y, 
                       xtest_tfidf)

print("Accuracy :  ",accuracy)


# Linear Classifier
accuracy = train_model(linear_model.LogisticRegression(),
                       xtrain_tfidf,
                       train_y,
                       xtest_tfidf)

print("Accuracy :  ",accuracy)














































