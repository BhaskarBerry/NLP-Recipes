# -*- coding: utf-8 -*-
"""
Building a End to End Text Preprocessing Pipeline


"""

sample = "How to take control of your #debt https://personal.vanguard.com/us/insights/saving-investing/ debt-management.# Best advice for #family #financial #success (@ PrepareToWin)"

def processRow(row):
    # import libraries
    import re
    import nltk
    from textblob import TextBlob,Word
    from nltk.corpus import stopwords
    from nltk.stem import PorterStemmer
    from nltk.util import ngrams
    from wordcloud import WordCloud, STOPWORDS
    from nltk.tokenize import word_tokenize
    
    tweet = row
    
    # lower case 
    tweet.lower()
    #Remove uincode character like "\u002c"
    tweet = re.sub(r'(\\u[0-9A-Fa-f]+)',r'',tweet)
    tweet = re.sub(r'[^\x00-\x7f]',r'',tweet)
    
    #convert any url to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert any @Username to "AT_USER"
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', '', tweet)
    tweet = re.sub('[\n]+', '', tweet)
    #Remove not alphanumeric symbols white spaces
    tweet = re.sub(r'[^\w]', '', tweet)
    #Removes hastag in front of a word """
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #Remove :( or :)
    tweet = tweet.replace(':)',"")
    tweet = tweet.replace(':(',"")
    #remove numbers
    tweet = " ".join([i for i in tweet if not i.isdigit()])
    #remove multiple exclamation
    tweet = re.sub(r"(\!)\1+", '', tweet)
    #remove multiple question marks
    tweet = re.sub(r"(\?)\1+", '', tweet)
    #remove multistop
    tweet = re.sub(r"(\.)\1+", '', tweet)
    #lemma
    tweet =" ".join([Word(word).lemmatize() for word in tweet.split()])
    #stemmer
    #st = PorterStemmer()
    #tweet=" ".join([st.stem(word) for word in tweet.split()])
    #Removes emoticons from text
    #tweet = re.sub(":\)|;\)|:-\)|\(-:|:-D|=D|:P|xD|X -p|\^\^|:-*|\^\.\^|\^\-\^|\^\_\^|\,-\)|\)-:|:\'\(|:\(|:-\(|:\S|T\.T|\.\_\.|:<|:-\S|:-<|\*\-\*|:O|=O|=\-O|O\.o|XO|O\_O|:-\@|=/|:/|X\-\ (|>\.<|>=\(|D:", '', tweet)
                                                                                                        
    #trim
    tweet = tweet.strip('\'"')
    row = tweet
    return row
    
#call the function with your data
processRow(sample)

            
    