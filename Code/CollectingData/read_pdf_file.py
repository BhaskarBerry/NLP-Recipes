# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 21:48:33 2021

@author: bberry
"""
import os
import PyPDF2
from PyPDF2 import PdfFileReader

path  = os.path.abspath("../../Data/StudentsData.pdf")

# create a PDF file Object
pdf = open(path, 'rb')

# create a PDF reader object
pdf_reader = PdfFileReader(pdf)

print(pdf_reader.numPages)

# creating a page object
page  = pdf_reader.getPage(0)

print(page.extractText())
print(page.extractText())

# closing the PDF file
pdf.close()
