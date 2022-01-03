# -*- coding: utf-8 -*-
"""
Extract Entities from Text - how to identify and extract entities
from the text, called Named Entity Recognition

There are multiple libraries to perform this task like 
NLTK chunker, StanfordNER, SpaCy, opennlp, and NeuroNER; 
and there are a lot of APIs also like WatsonNLU,
AlchemyAPI, NERD, Google Cloud NLP API, and many more


"""
import nltk
from nltk import ne_chunk
from nltk import word_tokenize

sent = "Berry is studing MTECH in IIT Kanpur at India"

# NER
ne_chunk(nltk.pos_tag(word_tokenize(sent)), binary=False)


# Using SpaCy
import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp(u'Apple is ready to launch new phone worth $10000 in New york time square ')

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
    
    

