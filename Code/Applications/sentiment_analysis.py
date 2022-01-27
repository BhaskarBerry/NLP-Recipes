# -*- coding: utf-8 -*-
"""
Sentiment Analysis:
    It is very important from a business standpoint to understand how customer 
    feedback is on the products/services they offer to improvise on the 
    products/service for customer satisfaction.

library: TextBlob or vaderSentiment

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import  os 

path = os.path.abspath("C:\Training2021\DataSet\Reviews.csv")

df = pd.read_csv(path)

df.head()
df.info()
df.Summary.head(5)
df.Text.head(5)


