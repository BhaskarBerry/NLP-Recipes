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
import pandas as pd

def co_occurance_matrix(corpus):
    vocab = set(corpus)
    vocab = list(vocab)
    vocab_to_index = {word:i for i ,word in enumerate(vocab)}
    
    # Create bigrams from all words in corpus
    bi_grams = list(bigrams(corpus))
    
    # Frequency distribution of bigrams((word1, word2),num_occurances)
    bigram_freq = nltk.FreqDist(bi_grams).most_common(len(bi_grams))
    
    # Initialise co-occurance matrix
    co_matrix = np.zeros((len(vocab), len(vocab)))
    
    for bigram in bigram_freq:
        current = bigram[0][1]
        previous = bigram[0][0]
        count = bigram[1]
        pos_current = vocab_to_index[current]
        pos_previous = vocab_to_index[previous]
        co_matrix[pos_current][pos_previous] = count
    
    co_matrix = np.matrix(co_matrix)
    
    return co_matrix,vocab_to_index
        
sen = [['I','like', 'NLP'],['I', 'Like','to','learn'],['nlp', 'is','cool'],
       ['nlp', 'is', 'future'],['nlp', 'is', 'cool']]

merged = list(itertools.chain.from_iterable(sen))
matrix = co_occurance_matrix(merged)

coMatrixFinal = pd.DataFrame(matrix[0], index = matrix[1],columns = matrix[1])

print(coMatrixFinal)
       
    
    
    
    
