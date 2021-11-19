# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 22:36:14 2021

@author: bberry
re - regular expression
"""
import re

text = """Challenges in natural language processing frequently involve speech recognition, natural language understanding, and 
natural language generation."""
        
#print(text)
"""
re.match(): This checks for a match of the string only
at the beginning of the string. So, if it finds the pattern
at the beginning of the input string, then it returns the
matched pattern; otherwise; it returns a none
"""
print(re.match("Cha", text))

"""
re.search(): This checks for a match of the string
anywhere in the string. It finds all the occurrences of
the pattern in the given input string or data.
"""
print(re.search("in", text))

# Tokenization
# Run the split query
t = re.split("\s+",text)
 
# Extrating Email ID

doc = "Reach me at : abc@abc.com, xyx@xyz.com"

mailID = re.findall(r'[\w\.-]+@[\w\.-]+', doc)

for mail in mailID:
    print(mail)


# Replacing the mail ID 

newMailID = re.sub(r'[\w\.-]+@[\w\.-]+', 
                   r'bberry@abc.com', doc)
print(newMailID)