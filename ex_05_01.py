# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 16:34:30 2018

@author: Randy
"""

num = 0
tot = 0.0
while True :
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
#    print(fval)
    num = num + 1
    tot = tot + fval
    
#print('ALL DONE')
print(tot,num,tot/num)


largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        fval = int(num)
    except:
        print('Invalid input')
        continue    
    if smallest is None:
        smallest = fval
    elif fval < smallest:
        smallest = fval
    if largest is None:
        largest = fval
    elif fval  > largest:
        largest = fval

print("Maximum is", largest)
print("Minimum is", smallest)


