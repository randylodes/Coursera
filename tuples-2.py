# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 06:12:43 2018

@author: Randy
"""


# Tuples can be on the both sides of a statement
(x, y) = (4, 'fred')
print(y)

# the dictionaries method items() returns a list of two-tuples (k, v)
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print(k,v)
    
tups = d.items()
type(tups)
print(tups)

# tupoles are comparable; uses most significant digit
(0,1,2) < (5,1,2)
(0,1,20000) < (0,3,4)
('Jones','Sally') < ('Jones','Sam')
('Jones','Sally') < ('Adams','Sam')

# sorting lists of tuples to get a sorted version of a dictionary
d = {'a':10, 'b':1, 'c':22}
print(d.items())
d2 = sorted(d.items()) # sorts on the key (most significant value)
print(d2) 

# using a loop
for k,v in d2:
    print(k,v)
    
# how to sort a dict on value insted of key
tmp = list()
for k,v in d.items():
    tmp.append((v,k))
print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)
