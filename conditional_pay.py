# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 15:19:05 2017

@author: Randy
"""

hrs = input("Enter Hours: ")
h = float(hrs)
rate = input("Enter Rate: ")
r = float(rate)

if h > 40:
    ot = h - 40
    pay = (r * 40.0) + (1.5 * r * ot)
else:
    pay = (r * h)
print(pay)
