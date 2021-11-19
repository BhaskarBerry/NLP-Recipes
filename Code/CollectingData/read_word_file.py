# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 22:03:01 2021

@author: bberry
"""
# install docx - pip install docx
# pip install python-docx 
from .exceptions import SendsayAPIError
import docx
from docx import Documnet

#Creating a word file object
doc = open("studentData.docx","rb")

#creating word reader object
document = docx.Document(doc)
"""
create an empty string and call this document. This document
variable store each paragraph in the Word document.We then
create a for loop that goes through each paragraph in the Word
document and appends the paragraph.
"""
docu=""
for para in document.paragraphs:
docu += para.text

#to see the output call docu
print(docu)

