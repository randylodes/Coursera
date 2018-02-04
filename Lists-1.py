# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 13:51:39 2018

@author: Randy
"""

# Mutable means changable
# strings are immutable; lists are mutable

fruit = ['apple','banana','pear']
fruit[2] = 'cherry'
print(fruit) 

x = [1,2,'joe',99]
print(len(x))

# range function returns a type 'range' (not list)
print(range(4))

for i in range(0,10):
    print(i)
print('\n')


# Using range() in a counted loop
friends = ['Joseph','Glenn','Sally']
for i in range(len(friends)) :
    print('Happy New Year', friends[i],'!')
    