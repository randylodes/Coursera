# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 13:56:16 2018

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

# Prefixes (commony used on for loop)
line = 'Please have a nice day'
if line.startswith('Please'):
    print('yes')

# Parsing and extracting (a common task)
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos) # starts search from the 2nd arg
print(sppos)
host = data[atpos+1 : sppos]
print(host)

# in Python3 all strings are Unicode 
# (much easier to work with than Python2)