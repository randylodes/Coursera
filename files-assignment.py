# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 09:13:00 2018

@author: Randy
"""

#==============================================================================
# 7.1 Write a program that prompts for a file name, 
# then opens that file and reads through the file, 
# and print the contents of the file in upper case. 
# Use the file words.txt to produce the output below.
# You can download the sample data at http://www.py4e.com/code3/words.txt
#==============================================================================

# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('Cannot open file', fname)
    quit()
for line in fh:
    line = line.strip()
    print(line.upper())
