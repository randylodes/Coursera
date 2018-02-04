# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 06:45:42 2017

@author: Randy
"""

score = input("Enter Score: ")
s = float(score)

if s > 1.0:
    print('Out of range. Please enter a score between 0.0 and 1.0')
    quit()

if s >= 0.9:
    grade = 'A'
elif s >= 0.8:
    grade = 'B'
elif s >= 0.7:
    grade = 'C'
elif s >= 0.6:
    grade = 'D'
else:
    grade = 'F'

print(grade)
