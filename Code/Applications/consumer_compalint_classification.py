# -*- coding: utf-8 -*-
"""
Problem:
Each week the Consumer Financial Protection Bureau sends thousands
of consumers’ complaints about financial products and services to
companies for a response. Classify those consumer complaints into the
product category it belongs to using the description of the complaint

Solution:
The goal of the project is to classify the complaint into a specific product
category. Since it has multiple categories, it becomes a multiclass
classification that can be solved through many of the machine learning
algorithms.
Once the algorithm is in place, whenever there is a new complaint,
we can easily categorize it and can then be redirected to the concerned
person. This will save a lot of time because we are minimizing the human
intervention to decide whom this complaint should go to.
"""

import os

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import string

from nltk.stem import SnowballStemmer, PorterStemmer
from nltk.corpus import stopwords
from textblob import TextBlob, Word

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, linear_model, naive_bayes,metrics, svm
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score

from io import StringIO

path = os.path.abspath("../../Data/TextClassification/consumer_complaints.csv")
data = pd.read_csv(path, encoding='latin-1')

data.dtypes
data.info()

Data = data[['product', 'consumer_complaint_narrative']]
Data.info()
Data = Data[pd.notnull(Data['consumer_complaint_narrative'])]
Data.head()

# Factorizing the category column
Data['category_id'] = Data['product'].factorize()[0]
Data.head()

Data.groupby('product').consumer_complaint_narrative.count()

# Plot
fig = plt.figure(figsize=(8,6))
Data.groupby('product').consumer_complaint_narrative.count().plot.bar(ylim=0)
plt.show()

# split the data
train_x, test_x, train_y, test_y = train_test_split(
    Data['consumer_complaint_narrative'], Data['product'])

# Feature Enginering using tfidf
encoder = preprocessing.LabelEncoder()
train_y = encoder.fit_transform(train_y)
test_y = encoder.fit_transform(test_y)

tfidf_vect = TfidfVectorizer(analyzer='word', max_features=5000,
                             token_pattern=r'\w{1,}')
tfidf_vect.fit(Data['consumer_complaint_narrative'])
xtrain_tfidf = tfidf_vect.transform(train_x)
xtest_tfidf = tfidf_vect.transform(test_x)

# Model building and evaluation
model = linear_model.LogisticRegression().fit(xtrain_tfidf, train_y)

# Model Summary
LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
                   intercept_scaling = 1, max_iter=100, multi_class='ovr',
                   n_jobs=1, penalty = 'l2',random_state= None,
                   solver='liblinear',tol= 0.0001)

#Checking Accuracy
accuracy = metrics.accuracy_score(model.predict(xtest_tfidf), test_y)
print("Accuracy: ", accuracy)

#Classification Report
print(metrics.classification_report(test_y,model.predict(xtest_tfidf),
                                    target_names = Data['product'].unique()))


conf_matrix = metrics.confusion_matrix(test_y,model.predict(xtest_tfidf))

# visualize Confusion matrix
category_id_df = Data[['product', 'category_id']].drop_duplicates(
    ).sort_values('category_id')
category_to_id = dict(category_id_df.values)
id_to_category = dict(category_id_df[['category_id','product']].values)

fig,ax = plt.subplots(figsize = (8,6))
sns.heatmap(conf_matrix, annot=True, fmt='d',cmap="BuPu",
            xticklabels=category_id_df[['product']].values,
            yticklabels=category_id_df[['product']].values)

plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show()

# Prediction example
texts = ["This company refuses to provide me verification and \
         validation of debt"+ "per my right under the FDCPA. \
         I do not believe this debt is mine."]
         
text_features = tfidf_vect.transform(texts)
predictions = model.predict(text_features)
print(texts)
print(" - Predicted as: '{}'".format(id_to_category[predictions[0]]))



"""
To increase the accuracy, we can do the following things:
• Reiterate the process with different algorithms like
Random Forest, SVM, GBM, Neural Networks, Naive
Bayes.
• Deep learning techniques like RNN and LSTM (will be
discussed in next chapter) can also be used
• In each of these algorithms, there are so many
parameters to be tuned to get better results. It can be
easily done through Grid search, which will basically
try out all possible combinations and give the best out.

"""













































