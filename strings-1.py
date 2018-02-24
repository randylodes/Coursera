# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 12:36:19 2018

@author: Randy
assignment 10.2
"""



# Subset a string with square brackets
fruit = "banana"
letter = fruit[1] # "fruit sub 1"
print(letter)


# The index can be computed
x = 3
w = fruit[x - 1]
print(w)
print() 
    
# The length function 
for i in range(0, len(fruit)-1):
    letter = fruit[i]
    print(letter)

print()

# Another way to construct the loop
index = 0 
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)    
    index = index + 1
print() 

# Or an even simpler way with a determinate loop
for letter in fruit:
    print(letter)
print() 

# Looping and counting
count = 0
for letter in fruit:
    if letter == 'a':
        count = count +1
print(count, "occurences of the letter a")
print()
