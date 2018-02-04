# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 07:30:23 2018

@author: Randy
"""


# Newline characters
stuff = 'Hello\nWorld'
print(stuff)

# Using the open() function
# handle = open(filename, mode)
fhand = open('mbox.txt', 'r')
print(fhand)

# Counting
count = 0
#print('Counting the lines..')
#for line in fhand:
    # print(line)
#    count = count +1
#print('Line count:', count)

# read the whole file with .read() method
# content including newlines is a single string 
print('..or all at once')
fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print(inp[:30])

# Searching in a file
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip() # remove the embedded newline 
    if line.startswith('From:') :
        print(line)

# Skipping lines with continue
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip() # remove the embedded newline 
    if not line.startswith('From:') :
        continue
    print(line)

# Using in to select lines
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip() # remove the embedded newline 
    if not '@uct.ac.za' in line :
        continue
    print(line)
    
    
# Prompt for file name from input
# and use error handling for bad file name
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    #quit()
    #exit()
   
    
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print('There are', count, 'subject lines in', fname)