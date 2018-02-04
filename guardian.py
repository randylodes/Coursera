# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 10:19:16 2018

@author: Randy
"""

han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
    # The guardian checks for both conditions (in order)
    # the opposite order wouldn't work..
    if len(wds) < 3 or wds[0] != 'From' : continue
    print(wds[1])