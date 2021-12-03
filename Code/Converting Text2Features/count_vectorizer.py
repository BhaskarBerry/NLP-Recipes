# -*- coding: utf-8 -*-
"""
Converting Text to Features Using Count Vectorizing

In one hot encoding - It does not take the frequency of the word occurring 
into consideration. 
If a particular word is appearing multiple times, there is a chance of
missing the information if it is not included in the analysis.

Count vectorizer is almost similar to One Hot encoding. The only
difference is instead of checking whether the particular word is present or
not, it will count the words that are present in the document

using --> sklearn-> CountVectorizer
"""
from sklearn.feature_extraction.text import CountVectorizer

text = ["I Like NLP and we can learn NLP in couple of months"]
# create a transformer
vect = CountVectorizer()

vect.fit(text)

# endcode doc
vector = vect.transform(text)

# summarize and generating output
print(vect.vocabulary_)
print(vector.toarray())

