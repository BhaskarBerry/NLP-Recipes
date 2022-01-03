# -*- coding: utf-8 -*-
"""
Part of Speech - Tagging

POS is the base for Named Entity Resolution,Sentiment Analysis, 
Question Answering, and Word Sense Disambiguation.

There are 2 ways a tagger can be built.
• Rule based - Rules created manually, which tag a word belonging to a particular POS.
• Stochastic based - These algorithms capture the sequence of the words and tag 
    the probability of the sequence using hidden Markov models.
    
Below are the short forms and explanation of POS tagging. The word
“love” is VBP, which means verb, sing. present, non-3d take.
• CC coordinating conjunction
• CD cardinal digit
• DT determiner
• EX existential there (like: “there is” ... think of it like
“there exists”)
• FW foreign word
• IN preposition/subordinating conjunction
• JJ adjective ‘big’
• JJR adjective, comparative ‘bigger’
• JJS adjective, superlative ‘biggest’
• LS list marker 1)
• MD modal could, will
• NN noun, singular ‘desk’
• NNS noun plural ‘desks’
• NNP proper noun, singular ‘Harrison’
• NNPS proper noun, plural ‘Americans’
• PDT predeterminer ‘all the kids’
• POS possessive ending parent’s
• PRP personal pronoun I, he, she
• PRP$ possessive pronoun my, his, hers
• RB adverb very, silently
• RBR adverb, comparative better
• RBS adverb, superlative best
• RP particle give up
• TO to go ‘to’ the store
• UH interjection
• VB verb, base form take
• VBD verb, past tense took
• VBG verb, gerund/present participle taking
• VBN verb, past participle taken
• VBP verb, sing. present, non-3d take
• VBZ verb, 3rd person sing. present takes
• WDT wh-determiner which
• WP wh-pronoun who, what
• WP$ possessive wh-pronoun whose
• WRB wh-adverb where, when
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize

Text = "I Like NLP , and striving to learn it in two months"

stop_words = set(stopwords.words('english'))

# Tokenize the text
tokens = sent_tokenize(Text)

# Generate tagging for all the tokens using loop
for i in tokens:
    words = nltk.word_tokenize(i)
    words = [w for w in words if not w in stop_words]
    
    # POS_Tagger
    tags = nltk.pos_tag(words)
tags    
    
