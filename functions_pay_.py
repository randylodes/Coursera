# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 15:19:05 2017

@author: Randy
"""

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    h = float(hrs)
    r = float(rate)
except:
    print('Invalid input. PLease enter input as a numerical format')
    quit()

def compute_pay(h, r):
    if h > 40:
        ot = h - 40
        p = (r * 40.0) + (1.5 * r * ot)
    else:
        p = (r * h)
    return p

pay = compute_pay(h, r)

print("Total pay is: " , pay)

