# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 14:55:04 2017

@author: Randy
"""

rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
except:
    ival = -1
    
if ival > 0 :
    print('Nice work')
else:
    print('Invalid input')