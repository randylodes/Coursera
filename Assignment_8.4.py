# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 08:48:05 2018

@author: Randy
"""

#==============================================================================
# 8.4 Open the file romeo.txt and read it line by line. For each line, split the
#  line into a list of words using the split() method. The program should build a
#  list of words. For each word on each line check to see if the word is already 
#  in the list and if not append it to the list. When the program completes, sort
#  and print the resulting words in alphabetical order.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt
#==============================================================================

#fname = 'romeo.txt'
fname = input("Enter file name: ")

# Open file handle
fh = open(fname)

# Initialize an empty list
word_list = list()

# Main loop
for line in fh:
    words = line.split()
    for word in words:
        if not word in word_list:
            word_list.append(word)
            #print('Appending', word)

# Alphabetizing
word_list.sort()

# Print final output
print(word_list)
            