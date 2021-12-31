# -*- coding: utf-8 -*-
"""
https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit

"""
import gensim

model = gensim.models.KeyedVectors.load_word2vec_format("C:\\Training2021\\Word2Vec_PreTrained_Model\\GoogleNews-vectors-negative300.bin",
    binary = True)

#Similarity Check

print(model.similarity('this','is'))

print(model.similarity('post','book'))

print(model.similarity('berry','berry'))

# Finding odd one
model.doesnt_match('morning afternoon snack evening'.split())

# Finds relations between words
model.word_vectors.most_similar(positive = ['woman','king'], negative = ['man'])


