# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 19:18:52 2018

@author: Randy
"""

import sys
import getopt


print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: " , sys.argv)
print(type(sys.argv))
print(sys.argv[1:])

#getopt.getopt(args, shortopts, longopts=[])

my_args = sys.argv[1:]
shortopts = 'a:b:c:d:'
optlist, args = getopt.getopt(my_args, shortopts)
print(optlist)
print(type(optlist))
print(args)
print(type(args))

