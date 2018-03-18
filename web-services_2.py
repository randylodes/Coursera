# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 07:10:10 2018

@author: Randy
"""

# parsing XML in Python
import xml.etree.ElementTree as ET

# a triple-quoted string can be multi-line
data = '''<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data) # tree is an XML object
name = tree.find('name').text # returns the text
email_attribute = tree.find('email').get('hide') # returns the attribute
print('name:',name)
print('email attribute:',email_attribute,'\n')


# when there are multiple child tags
my_input = '''<stuff>
   <users>
      <user x="2">
         <id>001</id>
         <name>Chuck</name>
      </user>
      <user x="7">
         <id>009</id>
         <name>Brent</name>
      </user>
   </users>
</stuff>'''

stuff = ET.fromstring(my_input)
lst = stuff.findall('users/user') # returns a list of <user> tags
print('User count:', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))