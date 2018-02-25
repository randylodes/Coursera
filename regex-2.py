# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 09:51:10 2018

@author: Randy

========================

^ beginning of line
$ end of line
. any character
\s whitespace
\S non-whitespace
* repeat a char zero or more times
*? non-greedy version of above
+ repeat a char one or more times
+? non-greedy version
[aeiou] match a single charater in set
[^XYZ] match a single character NOT in set
[a-z0-9] the set can include a range
( indicates where string extraction starts
) indicates where string extraction ends

"""

# re.search() returns True/False
# to return actual values, we use re.findall()

# square bracket [0-9] is like a single character
# this example will extract all instances of numbers in this string

import re
x = 'my 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
z = re.findall('AEIOU', x)
print(y)
print(type(y))
print(y[1])
print(type(y[1]))
print(z) # this will be an empty list

# greedy vs non-greedy matching 
# refers to the repeat special characters (* and +)
# pushing outward in both directions to match the largest possible string

x = 'From: Using the : character'
y = re.findall('^F.+:', x) # greedy
z = re.findall('^F.+?:', x) # non-greedy
print(y)
print(z)

# fine tuning the extracted portion using parentheses
# the parens are not part of the match; they define what is extracted
handle = open('mbox-short.txt')
for line in handle:
    line = line.rstrip()
    y = re.findall('\S+@\S+', line)
    if len(y) >0 : print(y)

handle = open('mbox-short.txt')
for line in handle:
    line = line.rstrip()
    y = re.findall('^From (\S+@\S+)', line) # the () defines what is returned 
    if len(y) >0 : print(y)
        
handle = open('mbox-short.txt')
for line in handle:
    line = line.rstrip()
    y = re.findall('@(\S+)', line) # or '@[^ ]*)'
    z = re.findall('^From .*@(\S+)', line) # same thing but more specific search
    if len(z) >0 : print(z)
        
numlist =  list()        
handle = open('mbox-short.txt')
for line in handle:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))

# escape character is a backslash \
x = 'We just recieved $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print(y[0])

a = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
b = re.findall('\S+@\S+', a)
c = re.findall('\S+?@\S+', a)
print(b)
print(c)