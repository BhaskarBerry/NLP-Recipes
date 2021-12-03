# -*- coding: utf-8 -*-
"""
Converting Text to Features
> Using One Hot Encoding
It is a process of converting categorical variables into features or columns 
and coding one or zero for the presence of that particular category.

One Hot Encoding will basically convert characters or words into binary
numbers

"""
import pandas as pd

Text = "I love learning NLP and NLP is future"

pd.get_dummies(Text.split())
