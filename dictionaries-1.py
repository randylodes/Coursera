# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 10:45:19 2018

@author: Randy
"""

# Lists retain their order
# Dictionary is a 'bag' of things with labels(key/value pairs)
# It is an example of an associative array

purse = dict() 
# or purse ={} 
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])

purse['candy'] = purse['candy'] + 2
print(purse['candy'])

# Dictionary literals (constants)
# {'key1' : value, 'key2' : value, ...}

jjj = { 'chuck' : 1, 'fred' : 42, 'jan' : 100}
print(type(jjj))
print(jjj)
ooo = {}
print(ooo)