# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 18:47:55 2018

@author: Randy
"""

#==============================================================================
# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html 
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this 
# process 4 times. The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah 
# Last name in sequence: Anayah

# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Lumi.html 
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this 
# process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: M

#==============================================================================

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
url = 'http://py4e-data.dr-chuck.net/known_by_Lumi.html'
position = 18 # starting position
count = 7 # how many interations 

while count > 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[position-1].get('href', None)
    print(url)
    count = count - 1

final_name = re.findall("known_by_(\S+?)\.html", url)
print('Final Name: ', final_name[0])