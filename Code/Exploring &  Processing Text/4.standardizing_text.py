# -*- coding: utf-8 -*-
"""
Standardizing Text
-using short words and abbreviations to
represent the same meaning
--own custom dictionary to look for short words and
abbreviations.
"""
import re

lookup_dict ={'wbu':"What about you",
              "ur": "your",
              "nlp": "natural language processing"}


def std_text(input_text):
    words = input_text.split()
    new_words = []
    for w in words:
        word = re.sub(r'[^\w\s]', '', w)
        if word.lower() in lookup_dict:
            word = lookup_dict[word.lower()]
            new_words.append(word)
            new_text = " ".join(new_words)
    return new_text


print(std_text("I like NLP its ur choice"))
