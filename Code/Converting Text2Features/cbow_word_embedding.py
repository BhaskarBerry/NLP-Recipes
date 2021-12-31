# -*- coding: utf-8 -*-
"""
Continuous bag of Words - CBOW 

"""

from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt

sentences = [['I', 'love', 'nlp'],
['I', 'will', 'learn', 'nlp', 'in', '2','months'],
['nlp', 'is', 'future'],[ 'nlp', 'saves', 'time', 'and', 'solves',
'lot', 'of', 'industry', 'problems'],['nlp', 'uses', 'machine', 'learning']]

cbow = Word2Vec(sentences ,vector_size = 50, window=3, min_count=1, sg=1)

print(cbow.wv['nlp'])

# save model
cbow.save('cbow.bin')
# load model
cbow = Word2Vec.load('cbow.bin')
# T – SNE plot
X = cbow[cbow.wv.vocab]
pca = PCA(n_components=2)
result = pca.fit_transform(X)
# create a scatter plot of the projection

plt.scatter(result[:, 0], result[:, 1])
words = list(cbow.wv.vocab)
for i, word in enumerate(words):
    plt.annotate(word, xy=(result[i, 0], result[i, 1]))
plt.show()