# -*- coding: utf-8 -*-
"""

Tokenization refers to splitting text into minimal meaningful units. 
There is a sentence tokenizer and word tokenizer.

libraries --> nltk, spacy and Textblob

"""

import pandas as pd
from textblob import TextBlob
import nltk


text = ['This is introduction to NLP','It is likely to be useful,to people '
        ,'Machine learning is the new electrcity',
        'There would be less hype around AI and more action goingforward',
        'python is the best tool!','R is good langauage','I like this book',
        'I want more books like this']

df = pd.DataFrame({"text":text})
df.head()

#using textblob
TextBlob(df["text"][3]).words

#using nltk
nltk.word_tokenize(df["text"][1])
nltk.word_tokenize("HI this is berry!")


#using split function from python
my_text = "HI this is berry!"
my_text.split()