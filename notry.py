# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 14:44:46 2017

@author: Randy
"""

astr = 'Hello Bob'
try: 
    istr = int(astr)
except:
    istr = -1
print(istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1

print(istr)

 
