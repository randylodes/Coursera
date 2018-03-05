# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 13:37:33 2018

@author: Randy
"""

# this library wraps the earlier socket actions for common HTTP functions
# no need to import socket() library

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())  # the line is still a byte string
    
# The above construct is similar to file open, and
# subsequent actions will be much like working with a local file
    

# Reading web pages (like a web browser)
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())
    
# Web scraping or 'spidering' 
#  -- how to parse the HTML? (it is full of errors and challenges)
# Use the BeautifulSoup library, made just for this (must install it first)
# conda install -c anaconda beautifulsoup4 

from bs4 import BeautifulSoup 

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrive all the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

# print(type(soup)) # it's an object returned from BS 
# print(type(tag)) # also an object

# additional code to handle SSL certificate errors
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# notes on the sample code and library versions:
#==============================================================================
# The sample code for this course and textbook examples use BeautifulSoup to parse HTML. The examples in the textbook and in this class work with BeautifulSoup 3 which only supports Python 2. To run the examples in this class, you have one of two choices.
# 
# Use a version of BeautifulSoup 3 that we have converted to Python 3
# Adapt our sample code to use BeautifulSoup 4
# Using BeautifulSoup 3
# 
# If you want use our samples "as is", download our Python 3 version of BeautifulSoup 3 from
# 
# http://www.py4e.com/code3/bs4.zip
# 
# You must unzip this into a "bs4" folder and have that folder as a sub-folder of the folder where you put our sample code like:
# 
# http://www.py4e.com/code3/urllinks.py
# 
# Using BeautifulSoup 4
# 
# You can download BeautifulSoup 4 from http://www.crummy.com/software/BeautifulSoup/ and follow the instructions there for installation. You will also need to adapt our sample code to make it work with the Python 3.0 BeautifulSoup library. The syntax will be different and that syntax is not supported by the course materials. Please note that the staff will not be able to help you with any issues you might encounter using either Python 3.x or BeautifulSoup 4.
#==============================================================================

    
    

    