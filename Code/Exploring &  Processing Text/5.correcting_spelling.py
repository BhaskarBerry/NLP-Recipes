# -*- coding: utf-8 -*-
"""
spelling correction
Typo error -- helps in reducing duplicate words

-- By using TextBlob library
pip install textblob

-- By using autocorrect library
pip intall autocorrect

"""

import pandas as pd
from textblob import TextBlob
from autocorrect import spell

text =['Introduction to NLP',
       'It is likely to be useful, topeople ',
       'Machine learning is the new electrcity', 
       'R is good langauage','I like this book']

df = pd.DataFrame({"msg":text})

df.head()

df["msg"] = df["msg"].apply(lambda x: str(TextBlob(x).correct()))

df.head()

print(spell("Hi msg mising srrviice mussage"))                


