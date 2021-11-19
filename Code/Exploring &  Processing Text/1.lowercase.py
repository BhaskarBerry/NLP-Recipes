# -*- coding: utf-8 -*-
"""
Convert text data to  lowercase -- lower()

x = 'LowER-Testing'
print(x.lower())

@author: bberry
"""

import pandas as pd

text = ['This is BERRY', 
        'Likes to Learn new concepts and explore latest technologies',
        'Like Python and Scala from Languages', 
        'Data is the new oil in the 21st century']

df = pd.DataFrame({'Data':text})

print(df)

df.head()

df.info()

df['Data'] = df['Data'].apply(lambda x: " ".join(x.lower() for x in x.split()))

df['Data']




