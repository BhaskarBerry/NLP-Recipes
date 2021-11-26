# -*- coding: utf-8 -*-
"""
Removing Stop words

Using NLTK library
"""
import pandas as pd
import nltk
#nltk.download()
from nltk.corpus import stopwords

test = ['This is introduction to NLP','It is likely to be useful,to people',
        'Machine learning is the new electrcity',
        'There would be less hype around AI and more action going forward',
        'python is the best tool!','R is good langauage','I likethis book',
        'I want more books like this']

# Convert list to data frame

df = pd.DataFrame({'msg':test})
#print(df)

stop = stopwords.words('english')

df["msg"] = df["msg"].apply(lambda x: " ".join(x for x in x.split() if x not in stop))

print(df["msg"])

 
