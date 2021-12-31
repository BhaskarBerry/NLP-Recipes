# -*- coding: utf-8 -*-
"""
fastText is another DL framework developed by Facebook to capture context and meaning.

fastText is the improvised version of word2vec. word2vec basically
considers words to build the representation. But fastText takes each
character while computing the representation of the word.

"""

from gensim.models import FastText
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
from gensim.models import Word2Vec

sentences = [['I', 'love', 'nlp'],
['I', 'will', 'learn', 'nlp', 'in', '2','months'],
['nlp', 'is', 'future'],[ 'nlp', 'saves', 'time', 'and', 'solves',
'lot', 'of', 'industry', 'problems'],['nlp', 'uses', 'machine', 'learning']]

fast = FastText(sentences,vector_size=20, window = 1, min_count = 1, 
                workers = 5, min_n = 1, max_n=2)

print(fast.wv['nlp'])

# load model
fast = Word2Vec.load('fast.bin')
# visualize
X = fast[fast.wv.vocab]
pca = PCA(n_components=2)
result = pca.fit_transform(X)

# create a scatter plot of the projection
plt.scatter(result[:, 0], result[:, 1])
words = list(fast.wv.vocab)
for i, word in enumerate(words):
    plt.annotate(word, xy=(result[i, 0], result[i, 1]))
plt.show()