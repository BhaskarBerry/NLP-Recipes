# -*- coding: utf-8 -*-
"""
want to extract or identify topics from the document - uisng genism lib
"""
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import gensim
from gensim import corpora


text = "I am learning NLP, it is very interesting and exciting. \
        it includes machine learning and deep learning"
doc2 = "My friend is a data scientist and he is nlp expert"
doc3 = "My sister has good exposure into android development"
doc_complete = [text, doc2, doc3]
doc_complete

# Text - Preprocessing
stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = " ".join([ch for ch in stop_free.split() if ch not in exclude])
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

doc_clean = [clean(doc).split() for doc in doc_complete]

# Creating the term dict of our corpus, where every unique term is assigned an index.
dictionary = corpora.Dictionary(doc_clean)

# Converting a list of documents (corpus) into Document-Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

doc_term_matrix

# LDA Model
Lda= gensim.models.ldamodel.LdaModel

ldamodel = Lda(doc_term_matrix, num_topics=3, id2word=dictionary, passes=50)

print(ldamodel.print_topics())
