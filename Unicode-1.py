# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 14:52:09 2018

@author: Randy
"""

# Many mappings of letters since the 70's
# ASCII (American Standard Code for information Interchannge) is the 
# most common mapping. Maps 128 numbers to a char set

# Python function 'ordinal' ord() will return the 8-bit (byte) ASCII number 0-256 
# Uppercase is lower number than lower
print(ord('H'))
print(ord('e'))
print(ord('\n'))

# Early international chacter sets were incompatible
# Unicode was created to addres this problem
# Covers many characters 

# Multi-byte characters - using more then 1 byte as previously
# UTF-8,16,32 is upward compatible with ASCII
# UTF-8 recommended for exchange between systems, become most popular
# a special bit makes UTF-8 variable length 1-2-4 bytes as needed

# In Python 3, all strings are Unicode Python (2 required extra conversion)
# byte string is another data type -- this is raw, unencoded
# when sending/receiving networked data, we must encode/decode strings
# by default, data.decode() assumes UTF-8 or ASCII
 # .encode() for sending bytes (default again is UTF-8)

