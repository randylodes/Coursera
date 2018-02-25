# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 09:14:55 2018

@author: Randy

===========================

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

For more information about using regular expressions in Python, 
see https://docs.python.org/3/howto/regex.html

"""


# The above is a partial list for reference
# regex can vary slightly between languages, but mostly similar
# think of regaex as it's own special language for character matching

# regex is very powerful, performing adavanced search task 
# using a reduced abount of code


# import the regex library
import re

# use re.search() method to see if a string matches a pattern\
# simmilar to find() 
# the two code examples below achieve the same thing

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line) :
        print(line)

# also similar
# line.startswith('From:')
# re.search('^From:', line)

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line) :
        print(line)

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X.*:', line) :
        print(line)

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X-\S+:', line) :
        print(line)


# use re.findall() to extract portions of a string that match a pattern
# similar to find() and slicing var[5:10]

 