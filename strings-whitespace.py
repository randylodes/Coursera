# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 13:51:31 2018

@author: Randy
"""

# Stripping whitespace with 'lstrip', 'rstrip', 'trip'
greet = '    Hello Bob   '
clean_greet = greet.lstrip()
print(clean_greet, 'X')
clean_greet = greet.rstrip()
print(clean_greet, 'X')
clean_greet = greet.strip()
print(clean_greet, 'X')
