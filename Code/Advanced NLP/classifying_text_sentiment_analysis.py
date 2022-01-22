# -*- coding: utf-8 -*-
"""
Text classification – The aim of text classification is to automatically classify
the text documents based on pretrained categories.

Sentiment Analysis :Sentiment analysis is one of the widely
used techniques across the industries to understand the sentiments of the
customers/users around the products/services. Sentiment analysis gives
the sentiment score of a sentence/statement tending toward positive or
negative.

- TextBlob or Vedar Library

• Polarity = Polarity lies in the range of [-1,1] where 1
means a positive statement and -1 means a negative
statement.
• Subjectivity = Subjectivity refers that mostly it is a
public opinion and not factual information [0,1].
"""
from textblob import TextBlob

# Sample Data
review = "I love this Phone. Screen quality and camera quality is really good"
review2 = "This tv is not good. Bad quality, no clarity, worst experience "

# TextBlob has a pre-trained sentiment prediction model
blob = TextBlob(review)
blob.sentiment

# output
# Sentiment(polarity=0.6, subjectivity=0.6000000000000001)

blob = TextBlob(review2)
blob.sentiment

# Output
# Sentiment(polarity=-0.6833333333333332, subjectivity=0.7555555555555555)

