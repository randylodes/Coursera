# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 11:23:47 2018

@author: Randy

Extracting Data With Regular Expressions
In this assignment you will read through and parse a file with text and numbers. 
You will extract all the numbers in the file and compute the sum of the numbers.
"""
# Sample data: regex_sum_42.txt (There are 90 values with a sum=445833)
# Actual data: regex_sum_56520.txt (There are 86 values and the sum ends with 3)

# Read through and parse a file with text and numbers. 
# Extract all the numbers in the file and compute the sum of the numbers.

import re

#fhandle = open('regex_sum_42.txt')
fhandle = open('regex_sum_56520.txt')
file = fhandle.read()
#print(file)

sum = 0
numlist = re.findall('[0-9]+', file)
#print(numlist)
for num in numlist:
    sum = sum + int(num)
print(sum)
