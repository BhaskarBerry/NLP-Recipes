# -*- coding: utf-8 -*-
"""
A count vectorizer and co-occurrence matrix have one limitation though.
In these methods, the vocabulary can become very large and cause
memory/computation issues.
One of the ways to solve this problem is a Hash Vectorizer.

HV - is mem efficient & instead of storing the tokens as strings, the vectorizer
applies the hashing trick to encode them as numerical indexes
The downside is that it’s one way and once vectorized,
the features cannot be retrieved.
"""

from sklearn.feature_extraction.text import HashingVectorizer

text = ["This is NLP course and easy to learn and good for the new apps"]

# create a hashing vectorizer
vectorizer = HashingVectorizer(n_features = 10)

# transform
vector = vectorizer.transform(text)

# summerize the vector
print(vector.shape)

print(vector.toarray())

