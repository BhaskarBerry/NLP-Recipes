# -*- coding: utf-8 -*-
"""
Previous method Drawbacks
> Fail to capture the context and meaning of words
> Doc Classification is huge and number of tokens generated gets out of control
hampering the accuracy and performance

Word Embedding:
    Word embedding is the feature learning technique where words from
the vocabulary are mapped to vectors of real numbers capturing the
contextual hierarchy.

Word embeddings are prediction based, and they use shallow neural
networks to train the model that will lead to learning the weight and using
them as a vector representation.

The skip-gram model is used to predict the probabilities of a word given the 
context of word or words.
"""
# pip install gensim
"""
import gensim
from gensim import interfaces, utils, matutils
from gensim.matutils import dirichlet_expectation, mean_absolute_difference
"""
from gensim.models import Word2Vec

from sklearn.decomposition import PCA
from matplotlib import pyplot

sentences = [['I', 'love', 'nlp'],
['I', 'will', 'learn', 'nlp', 'in', '2','months'],
['nlp', 'is', 'future'],
[ 'nlp', 'saves', 'time', 'and', 'solves','lot', 'of', 'industry', 'problems'],
['nlp', 'uses', 'machine', 'learning']]

skipgram = Word2Vec(sentences, vector_size=50,window=3,min_count=1,sg=1)
"""
Gensim 4.0 & higher, the Word2Vec model doesn't support subscripted-indexed 
access (the ['...']') to individual words. 
(Previous versions would display a deprecation warning, Method will be removed
in 4.0.0, use self.wv.getitem() instead`, for such uses.)
"""
print(skipgram.wv['nlp'])
print(skipgram["NLP"])
print(skipgram.wv['deep'])
#Save model
skipgram.save("skipgram.bin")

# Load model
sg_model = Word2Vec.load("skipgram.bin") 

#words = list(skipgram.wv.vocab)
words = list(sg_model.wv.key_to_index)
# T – SNE plot is one of the ways to evaluate word embeddings
X = words
pca = PCA(n_components=2)
result = pca.fit_transform(X)

# Scatter plot
pyplot.scatter(result[:,0], result[:,1])
words = list(skipgram.wv.vocab)
for i, word in enumerate(words):
    pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
pyplot.show()



