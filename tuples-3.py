# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 06:41:23 2018

@author: Randy
"""

# solving a problem: 10 most common words

f = 'romeo.txt'
fhand = open(f)

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

lst = list()
for k,v in counts.items():
    lst.append((v,k))

lst = sorted(lst, reverse=True)

for v,k in lst[:10]:
    print(k,v)

# alternatively, this last block could be done in one line of code
# using the python feature 'list comprehension'
# List comprehension makes a dynamic list of reversed tupoles then sorts it
print(sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )

# Read further on list comprehension coocept to better understand 