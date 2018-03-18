# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 08:24:43 2018

@author: Randy
"""
#==============================================================================
# look through all the <comment> tags, find the <count> values, and sum the numbers
# 
# structure will look like this:
# <comment>
#   <name>Matthias</name>
#   <count>97</count>
# </comment>
# 
# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_56524.xml (Sum ends with 8)
#
# API documentation for XML parsing module
# https://docs.python.org/3/library/xml.etree.elementtree.html
#==============================================================================


import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
url = 'http://py4e-data.dr-chuck.net/comments_56524.xml'
uh = urllib.request.urlopen(url)
data = uh.read()
# print(data)
tree = ET.fromstring(data)
lst = tree.findall('comments/comment') # returns a list of <comment> tags
total = 0
for tag in lst:
    num = int(tag.find('count').text)
    total = total + num
print('Count:', len(lst))
print('Sum:',total)


"""
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'
while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)

    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print('lat', lat, 'lng', lng)
    print(location)
""" 