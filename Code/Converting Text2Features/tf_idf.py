# -*- coding: utf-8 -*-
"""
tf_idf is to reflect on how imp a word is to a document in a collection
and normalizing  words appreared fre in all the doc

Term frequency (TF): Term frequency is simply the ratio of the count of a
word present in a sentence, to the length of the sentence.

Inverse Document Frequency (IDF): IDF of each word is the log of
the ratio of the total number of rows to the number of rows in a particular
document in which that word is present.

"""

from sklearn.feature_extraction.text import TfidfVectorizer

text = ["This is berry!! I love to learn and teach NLP with the latest applications"]

vectorizer= TfidfVectorizer()

# tokenize and build vocab
vectorizer.fit(text)
 
print(vectorizer.vocabulary_)
print(vectorizer.idf_)