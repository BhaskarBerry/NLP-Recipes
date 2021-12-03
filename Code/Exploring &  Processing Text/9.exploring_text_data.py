# -*- coding: utf-8 -*-
"""
Extracting the data : data collection and text processing

=> using NLTK , TextBlob lib

"""
#---- Import libraries
import nltk
from nltk.corpus import webtext
#nltk.download('webtext')
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string

wt_sen = webtext.sents('firefox.txt')
wt_words = webtext.words('firefox.txt')
#---------------------------------
len(wt_sen)
len(wt_words)

freq_dist = FreqDist(wt_words)
freq_dist 

sorted_freq_dist = sorted(freq_dist, key=freq_dist.__getitem__, reverse=True)
sorted_freq_dist
 
large_words = dict([(k,v) for k,v in freq_dist.items() if len(k) > 5])
fr_dist  = FreqDist(large_words)
fr_dist.plot(50, cumulative = False)
#---------------------------------

# Build Word Cloud
#pip install wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt

wcloud = WordCloud().generate_from_frequencies(fr_dist)

# plotting wordcloud
plt.imshow(wcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

