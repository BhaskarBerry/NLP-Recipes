# -*- coding: utf-8 -*-
"""
Extract a noun phrase from the text data

Noun Phrase extraction is important when you want to analyze the “who” in a sentence.
"""

import nltk
from textblob import TextBlob

# Extract Noun
blob = TextBlob("Berry has started learning natural language processing")

for np in blob.noun_phrases:
    print(np)