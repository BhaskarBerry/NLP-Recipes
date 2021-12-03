# -*- coding: utf-8 -*-
"""
Co-occurance matrix: is like a count vectorizer where it counts the
occurrence of the words together, instead of individual words.

using -> nltk, bigrams
"""
import numpy as np
import nltk
from nltk import bigrams
import itertools

def co_occurane_matrix(corpus):
    vocab = set(corpus)
    vocab = list(vocab)
    vocab_to_index = {word:i for i ,word in enumerate(vocab)}
    
