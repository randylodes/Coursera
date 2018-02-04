# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 09:17:48 2018

@author: Randy
"""

#==============================================================================
# 8.5 Open the file mbox-short.txt and read it line by line. When you find a
# line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word 
# in the line (i.e. the entire address of the person who sent the message). 
# Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'Fro
#==============================================================================

# fname = 'mbox-short.txt'
fname = input("Enter file name: ")

# open file handle
fh = open(fname)

# Initialize the counter
count = 0

# main loop
for line in fh:
    if not line.startswith('From '): continue
    email_address = line.split()[1]
    print(email_address)
    count = count + 1

# Print final count
print("There were", count, "lines in the file with From as the first word")
    
