# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 09:14:55 2018

@author: Randy
"""

# Constant syntax in Javascript
# not as 'rich' as XML, but simple and much easier to use
# if you *can* use JSON you should; or use XML if you must
# represents data as nested 'lists' and 'dictionaries'

import json

# curly braces like a python dictionary with key/value pairs
data = '''{
    "name" : "Chuck",
    "phone" :  {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
    "hide" : "yes"
    }
}'''
# can also think of this as a tree

# this actually creates a python dictionary
info = json.loads(data)  # this function loads from string
print('Name:',info["name"])
print('Hide:',info["email"]["hide"])

# this is a list of two dictionaries 
input = '''[
    { "id" : "001",
    "x" : "2",
    "name" : " Chuck"
    },
    { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
    }
]'''

info = json.loads(input)
print('User count:', len(info))
for item in info:
    print('Name:', item['name'])
    print('Id:', item['id'])
    print('Attribute:', item['x']) # no concept of attributes like in XML
    
    
