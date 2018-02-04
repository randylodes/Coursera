# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 13:31:57 2018

@author: Randy
"""

# Object method
greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print(greet)
print('Hi There'.lower())


# The 'dir' function shows the available methods
stuff = 'Hello World'
print(type(stuff))
print(dir(stuff))
print(stuff.upper())
print()

# a commonly used operator is 'find'
fruit = 'banana'
pos = fruit.find('na')
print(pos)
aa = fruit.find('z')
print(aa)

name = 'randy'
name_cap = name.capitalize()
print(name_cap)

# might use something like this to compare strings ignoring case
if name.lower() == name_cap.lower():
    print('match')

# Search and replace
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr)
nstr = greet.replace('o', 'X')
print(nstr)

