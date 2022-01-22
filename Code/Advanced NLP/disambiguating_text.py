# -*- coding: utf-8 -*-
"""
There is ambiguity that arises due to a different meaning of words in a
different context.

For example,
Text1 = 'I went to the bank to deposit my money'
Text2 = 'The river bank was full of dead fishes'
The word “bank” has different meanings based on the context of the sentence.


The Lesk algorithm is one of the best algorithms for word sense
disambiguation.
package pywsd and nltk.
from pywsd.lesk import simple_lesk

"""

from nltk.corpus import wordnet as wn
from nltk.stem import PorterStemmer
from itertools import chain
from nltk.wsd import lesk

# Disambiguating word sense

bank_sent = ['I went to the bank to deposit my money',
             'The river bank was full of dead fishes']

#Calling lesk function
print("context-1:", bank_sent[0])  
answer = lesk(bank_sent[0], 'bank')
print("Sense : ", bank_sent[0])
print("Definition : ", answer.definition())

print("context-2:", bank_sent[1])  
answer1 = lesk(bank_sent[1], 'bank')
print("Sense : ", bank_sent[1])
print("Definition : ", answer1.definition())

"""
context-1: I went to the bank to deposit my money
Sense :  I went to the bank to deposit my money
Definition :  a container (usually with a slot in the top) for keeping money at home
context-2: The river bank was full of dead fishes
Sense :  The river bank was full of dead fishes
Definition :  a container (usually with a slot in the top) for keeping money at home
"""