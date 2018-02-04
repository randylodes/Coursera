# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 11:20:27 2018

@author: Randy
"""

# Solving histogram type of problems
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)

# adding new names and counting
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

# there is a 'get' method in python that makes this easier
# this is a common dictionary/histogram idiom
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
        counts[name] = counts.get(name, 0) + 1
print(counts)

