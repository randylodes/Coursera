# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 13:04:01 2018

@author: Randy
"""

# Slicing strings
# The 2nd character means "up to but not including"
s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])
print()

# Can eliminate the prefix of suffix from the range
print(s[:2])
print(s[8:])
print(s[:])