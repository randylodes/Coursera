# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 11:46:52 2018

@author: Randy
"""

counts = dict()
#print('Enter a line of text:')
#line = input('')
line = 'Here you can get help of any object by pressing Ctrl+I in front of it, either on'
words = line.split()
print('Words: ', words)
print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts:', counts)

# Definite loops and dictionaries
counts = { 'chuck' : 1, 'fred' : 42, 'jan' : 100}
for key in counts:
     print(key, counts[key])

# getting lists from a dictionary
print(list(counts))
print(counts.keys())
print(counts.values())
print(counts.items()) # this prints a list of tuples

# looping with two iteration variables
for aaa,bbb in counts.items():
    print(aaa, bbb)

fname = 'words.txt'
fhandle = open(fname)

counts = dict()
for line in fhandle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print('Counts:', counts)

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print("The most frequent word '" + bigword + "' occured", bigcount, "times")