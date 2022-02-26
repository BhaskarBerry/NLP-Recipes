# -*- coding: utf-8 -*-
"""
Text summarization of article/document using different algorithms in Python.

Text summarization is the process of making large documents into smaller
ones without losing the context, which eventually saves readers time. This
can be done using different techniques like the following:
• TextRank: A graph-based ranking algorithm
• Feature-based text summarization
• LexRank: TF-IDF with a graph-based algorithm
• Topic based
• Using sentence embeddings
• Encoder-Decoder Model: Deep learning techniques

1. TextRank - Gensim It is basically
inspired by PageRank, which is used in the Google search engine but
particularly designed for text. It will extract the topics, create nodes out of
them, and capture the relation between nodes to summarize the text.
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen

from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords

# Get the data from wiki
def get_only_text(url):
    page = urlopen(url)
    soup = BeautifulSoup(page)
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    print(text)
    return soup.title.text, text

url = "https://en.wikipedia.org/wiki/Natural_language_processing"
text = get_only_text(url)
len(''.join(text))
text[:100]
text = str(text)

# summarize the text with ratio 0.1
summarize(text,0.1)
print(keywords(text, ratio=0.1))

"""
Feature based text summarization
Your feature-based text summarization methods will extract a feature from
the sentence and check the importance to rank it. Position, length, term
frequency, named entity, and many other features are used to calculate the
score.
Luhn’s Algorithm is one of the feature-based algorithms,
"""

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.summarizers.luhn import LuhnSummarizer

# extracting and summerizing
LANGUAGE = "english"
SENTENCES_COUNT = 10

parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
summarizer = LsaSummarizer()
summarizer = LsaSummarizer(Stemmer(LANGUAGE))
summarizer.stem_words = get_stop_words(LANGUAGE)
for sentence in summarizer(parser.document, SENTENCES_COUNT):
    print(sentence)
    


























































