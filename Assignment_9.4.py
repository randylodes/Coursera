# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 14:39:21 2018

@author: Randy
"""

#==============================================================================
# 9.4 Write a program to read through the mbox-short.txt and figure out who has 
# the sent the greatest number of mail messages. The program looks for 'From ' 
# lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to 
# a count of the number of times they appear in the file. After the dictionary is 
# produced, the program reads through the dictionary using a maximum loop to find 
# the most prolific committer.
#==============================================================================

# Get file name from input
fname = input("Enter file:")

# Use a default file name is user inputs no value
if len(fname) < 1 : fname = "mbox-short.txt"
# fname = 'mbox-short.txt'

# Open the file handle
fhandle = open(fname)

# Loop to build the count dictionary
count_dict = dict() 
for line in fhandle:
    if not line.startswith('From ') : continue
    line = line.strip()
    #print(line)
    email_address = line.split()[1]
    #print(email_address)
    count_dict[email_address] = count_dict.get(email_address, 0) + 1

#print(count_dict)
    
# Loop to analyze the dictionary for results
top_name = None
top_count = None
for k,v in count_dict.items():
    # print(k,v)
    if top_count is None or v > top_count:
        top_name = k
        top_count = v

print(top_name, top_count)
    