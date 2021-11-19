# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 22:18:21 2021

@author: bberry

using bs4 library

"""

# pip install bs4

import urllib.request as urllib2
from bs4 import BeautifulSoup

response  = urllib2.urlopen('https://en.wikipedia.org/wiki/Natural_language_processing')

html_doc = response.read()

# parsing
soup = BeautifulSoup(html_doc, 'html.parser')

#Formating the parsed html ile
str_html = soup.prettify() 

print(str_html[:2000])

"""
# Extract tag Value
print(soup.title)
print(soup.title.string)
print(soup.a.string)
print(soup.b.string)

for x in soup.find_all('a'):
    print(x.string)
"""

for x in soup.find_all('p'):
    print(x.text)
    