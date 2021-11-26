# -*- coding: utf-8 -*-
"""
Removing Punctuations

using -- regex and replace()
"""
import pandas as pd
import re
import string


s = "I. love . [This]*&%^&*^%^## Field!!!"
s1 = re.sub(r'[^\w\s]', '', s)
print(s1)
print("------------------------")

test_msg = ['This is Bhaskar Berry, ''',"I like ML! DL! NLP!",
            'Natural language Processing $ ', "Removing # &*(^8 5636"]

df = pd.DataFrame({'Message':test_msg})

print(df)
print("------------------------")
df['msg'] = df["Message"].str.replace('[^\w\s]', '')
print(df["msg"])

print("---Using string punctuation---------------------")
print("Before removing punctuation:" ,s)

for c in string.punctuation:
    s = s.replace(c,"")

s

print("After removing punctuation:" ,s)
print("------------------------")