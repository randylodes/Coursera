# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 05:51:51 2018

@author: Randy
"""

# A tuple can be thought af a special, unmodifiable (immutable) list
# Tuples are more efficient in terms of memory and performance
# preferred to use them for 'temporary variables'
 
# construction is similar to a list, but we use parens
# here, x is a 'three tuple' (a term from mathematics)
x = ('Glen', 'Sally', 'Joseph')

# functions like splitting, max, loop iteration, etc work same as lists
print(type(x))
print(x[1])

y = (1,9,2)
print(max(y))

for i in y:
    print(i)

# major difference is tuples are immutable
# this assignment statement will fail
# y[1] = 7

# cannot sort a tuple
# x.sort()

# what does tuple support? look at directory index
# valid methods incluse 'count' and 'index'
t = tuple()
print(dir(t))
