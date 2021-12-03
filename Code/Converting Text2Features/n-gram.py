# -*- coding: utf-8 -*-
"""
N-grams
Problem:
In Count vectorizer each word is considers as a future
It does not consider the previous or next word to give meaning
"not bad" --> good

Solution : N-grams
N-grams are the fusion of multiple letters or multiple words. 
They are formed in such a way that even the prev and next words are captured.
• Unigrams are the unique words present in the sentence.
• Bigram is the combination of 2 words.
• Trigram is 3 words and so on.
For example,
“I am learning NLP”
Unigrams: “I”, “am”, “ learning”, “NLP”
Bigrams: “I am”, “am learning”, “learning NLP”
Trigrams: “I am learning”, “am learning NLP”

using -> TextBlob other are also available
"""

from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer

Text = "I love my Country."

# For unigram : n=1
TextBlob(Text).ngrams(1)

# For bigram : n=2
TextBlob(Text).ngrams(2)

# For Trigram : n=3
TextBlob(Text).ngrams(3)


nt = ["I Like NLP and we can learn NLP in couple of months"]
#create a trasformer
vec = CountVectorizer(ngram_range=(2,2))

#tokenizing
vec.fit(nt)
vector = vec.transform(nt)
print(vec.vocabulary_)
print(vector.toarray())
