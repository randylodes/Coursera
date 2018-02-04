# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 07:18:44 2018

@author: Randy
"""

#==============================================================================
# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
#==============================================================================

# open the file
#f = 'mbox-short.txt'
f = input("Enter file:")
if len(f) < 1 : f = "mbox-short.txt"
fhandle = open(f)

# intitialize the dictionary 
counts=dict()

# main execution loop
for line in fhandle:
    if not line.startswith('From '): continue
    line = line.strip()
    time = line.split()[5]
    hour = time.split(':')[0]
    #print(hour)
    counts[hour] = counts.get(hour, 0) + 1

# initialize a temporary list
# lst = list()
lst = sorted(counts.items())
# print(lst)

# create a list of tuples
#for k,v in counts.items():
#    lst.append((k,v))
  
# sort the list on k
#lst = sorted(lst)

# print the output
for (k,v) in lst:
    print(k,v)