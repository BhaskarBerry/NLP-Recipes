# -*- coding: utf-8 -*-
"""
Lemmatizing:Lemmatization is a process of extracting a root word by considering 
    the vocabulary. For example, “good,” “better,” or “best” is lemmatized 
    into good.

Lemmatization in NLTK is the algorithmic process of finding the lemma of a 
word depending on its meaning and context

Lemmatization can get better results.
• The stemmed form of leafs is leaf.
• The stemmed form of leaves is leav.
• The lemmatized form of leafs is leaf.
• The lemmatized form of leaves is leaf.

=> using NLTK or the TextBlob library

Why is Lemmatization better than Stemming?
Stemming algorithm works by cutting the suffix from the word. 
In a broader sense cuts either the beginning or end of the word.
"""
import pandas as pd
from textblob import Word
from nltk.stem import WordNetLemmatizer

text_msg = ['I like fishing','I eat fish','There are many fishes in pound', 
            'leaves and leaf']

df = pd.DataFrame({'msg':text_msg})
df.head()

#code for lemmatize
df['msg'] = df['msg'].apply(
    lambda x : " ".join([Word(word).lemmatize() for word in x.split()]))

df['msg']

# Lemmatization
lemmatizer = WordNetLemmatizer()
print("rocks", lemmatizer.lemmatize("rocks"))
print("better", lemmatizer.lemmatize("better","a"))

