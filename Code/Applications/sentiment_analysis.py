# -*- coding: utf-8 -*-
"""
Sentiment Analysis:
    It is very important from a business standpoint to understand how customer 
    feedback is on the products/services they offer to improvise on the 
    products/service for customer satisfaction.

library: TextBlob or vaderSentiment

Sentiment Analysis: Pretrained model takes the input from the text
description and outputs the sentiment score ranging from -1 to +1 for each
sentence.

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import  os 

from nltk.corpus import stopwords
from textblob import TextBlob
from textblob import Word

from wordcloud import WordCloud
from wordcloud import STOPWORDS

import seaborn as sns
import re
import sys
import ast
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

plt.style.use('fivethirtyeight')
# Function for getting the sentiment
cp = sns.color_palette()

path = os.path.abspath("C:\Training2021\DataSet\Reviews.csv")
df = pd.read_csv(path)
df.head()
df.info()
df.Summary.head(5)
df.Text.head(5)

# Cleaning Text
df['Text'] = df['Text'].apply(lambda x: " ".join(x.lower() for x in x.split()))
df['Text'] = df['Text'].str.replace('[^\w\s]','')
df.Text.head(5)
stop = stopwords.words('english')
df['Text'] = df['Text'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))

df.Text.head(5)

# spelling correction
df['Text'] = df['Text'].apply(lambda x: str(TextBlob(x).correct()))

df.Text.head(5)
df['Text'] = df['Text'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))

# EDA
reviews = df
reviews.dropna(inplace = True)

reviews.Score.hist(bins= 5, grid= False)
plt.show()
print(reviews.groupby('Score').count().Id)

# To make it balanced data, we sampled each score by the lowest n-count from above. 
#(i.e. 29743 reviews scored as '2')
score_1 = reviews[reviews['Score'] == 1].sample(n=29743)
score_2 = reviews[reviews['Score'] == 2].sample(n=29743)
score_3 = reviews[reviews['Score'] == 3].sample(n=29743)
score_4 = reviews[reviews['Score'] == 4].sample(n=29743)
score_5 = reviews[reviews['Score'] == 5].sample(n=29743)

review_balanced_data = pd.concat([score_1, score_2, score_3, score_4, score_5], 
                                 axis = 0) 

review_balanced_data.reset_index(drop=True, inplace = True)
print(review_balanced_data.groupby('Score').count().Id)

review_str = review_balanced_data.Summary.str.cat()

word_cloud = WordCloud(background_color='white').generate(review_str)

plt.figure(figsize=(10,10))
plt.imshow(word_cloud,interpolation='bilinear')
plt.axis("off")
plt.show()

negative_reviews = review_balanced_data[review_balanced_data['Score'].isin([1,2])]
positive_reviews = review_balanced_data[review_balanced_data['Score'].isin([4,5])]

# Transform to a single string
negative_reviews_str = negative_reviews.Summary.str.cat()
positive_reviews_str = positive_reviews.Summary.str.cat()

wordcloud_negative = WordCloud(background_color='white').generate
(negative_reviews_str)
wordcloud_positive = WordCloud(background_color='white').generate
(positive_reviews_str)

# Plot
fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(211)
ax1.imshow(wordcloud_negative,interpolation='bilinear')
ax1.axis("off")
ax1.set_title('Reviews with Negative Scores',fontsize=20)


ax2 = fig.add_subplot(212)
ax2.imshow(wordcloud_positive,interpolation='bilinear')
ax2.axis("off")
ax2.set_title('Reviews with Positive Scores',fontsize=20)
plt.show()

# Sentiment Score
analyzer = SentimentIntensityAnalyzer()

# Generating sentiment for all the sentence present in the dataset
emptyline=[]
for row in df['Text']:
    vs=analyzer.polarity_scores(row)
    emptyline.append(vs)
    
# Creating new dataframe with sentiments
df_sentiments=pd.DataFrame(emptyline)
df_sentiments.head(5)

# Merging the sentiments back to reviews dataframe
df_c = pd.concat([df_sentiments.reset_index(drop=True), df], axis=1)
df_c.head(3)

# Convert scores into positive and negetive sentiments using some threshold
df_c['Sentiment'] = np.where(df_c['compound'] >= 0 , 'Positive','Negative')
df_c.head(5)

result=df_c['Sentiment'].value_counts()
result
result.plot(kind='bar', rot=0, color = "red");


#Sample code snippet
result=df_c.groupby('ProductId')['Sentiment'].value_counts().unstack()

result[['Negative','Positive']].plot(kind='bar',rot=0,color='rb').show()














