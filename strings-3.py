# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 12:36:18 2018

@author: Randy
"""

# Concatenation - use +
a = 'Hello'
b = 'There'
print(a + b)
print(a,b)
c = a + ' ' +b
print(c)
print()

# in as a logical operator
fruit = 'banana'
if 'n' in fruit:
    print('yes')
if 'nan' in fruit:
    print('yes')

# String comparison 
word = fruit
if word == 'banana':
    print('All right, bananas')

word = 'apple'
if word < 'banana':
    print('Your word, ' + word + ', comes before banana')

word = 'Peach'
if word < 'banana':
    print('Your word, ' + word + ', comes before banana')