# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 18:12:17 2018

@author: Randy
Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_56522.html (Sum ends with 76)

searching for lines in this format:
<tr><td>Modu</td><td><span class="comments">90</span></td></tr>
<tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
<tr><td>Hubert</td><td><span class="comments">87</span></td></tr>

You are to find all the <span> tags in the file and pull out the numbers from 
the tag and sum the numbers.
Look at the sample code provided. It shows how to find all of a certain kind of 
tag, loop through the tags and extract the various aspects of the tags.
"""

# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# url = 'http://py4e-data.dr-chuck.net/comments_42.html'
url = 'http://py4e-data.dr-chuck.net/comments_56522.html'

html = urlopen(url, context=ctx).read()

# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')

#  pull out the numbers from the tag and sum the numbers
total = 0
for tag in tags:
    # print('TAG:', tag)
    # print('Contents:', tag.contents[0])
    number = int(tag.contents[0])
    # print(number)
    total = total + number
print('Count', len(tags))
print('Sum', total)