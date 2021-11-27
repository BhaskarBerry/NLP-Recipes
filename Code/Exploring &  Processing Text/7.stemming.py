# -*- coding: utf-8 -*-
"""
Stemming: Stemming is a process of extracting a root word. 
For example, “fish,” “fishes,” and “fishing” are stemmed into fish.

-> Using NLTK or TextBlob lib

Stemming can lead to incorrect spelling and wrong meanings, but lemmatization gives a correct base form of a word. 

‘Sharing’ -> Stemming -> ‘Shar’
‘Sharing’ -> Lemmatization -> ‘Share’

"""
import pandas as pd
from textblob import Word
from nltk.stem import PorterStemmer

msg = ["I like eating pasta", 'I love to eats',
       'I like fishing','I eat fish',
       'There are many fishes in pound']

df = pd.DataFrame({'msg':msg})
print(df)

# Using Porter Stemmer
st = PorterStemmer()

df['msg1'] = df['msg'].apply(
    lambda x: " ".join([st.stem(word) for word in x.split()]))

print("After Applying Stemming!!!")

print(df.head())

# Using word
print(Word(df['msg'][0]).lemmatize())

u = Word("rocks")
print(u,":", u.lemmatize())

v = Word("better")
# Apply lemmatization with a  parameter "a" -> adjective
print(v,":", v.lemmatize("a"))

