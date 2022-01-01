# -*- coding: utf-8 -*-
"""
Cosine similarity: Calculates the cosine of the angle between the two vectors.
Jaccard similarity: The score is calculated using the intersection or union of words.
Jaccard Index = (the number in both sets) / (the number in either set) * 100.
Levenshtein distance: Minimal number of insertions, deletions, and replacements 
required for transforming string “a” into string “b.”
Hamming distance: Number of positions with the same symbol in both strings. 
But it can be defined only for strings with equal length

"""

from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = ("I like NLP","I am exploring NLP","I am a beginner in NLP",
"I want to learn NLP","I like advanced NLP")

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
tfidf_matrix.shape

cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)


"""
Phonetic matching - It is very useful for searching
large text corpora, correcting spelling errors, and matching relevant names.
Soundex and Metaphone are two main phonetic algorithms used for this purpose.
"""
