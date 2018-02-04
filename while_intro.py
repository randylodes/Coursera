# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 15:16:57 2018

@author: Randy
"""

# Simple iteration
n = 5
while n > 0 :
    print(n)
    n = n-1
print("Blastoff!")
    
# Break statement
while True:
    line = input('> ')
    if line == 'done' :
        break
    print(line)
print('Done!')

# Continue statement
while True:
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')


