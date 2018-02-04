# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 14:16:42 2018

@author: Randy

6.5 Write code using find() and string slicing (see section 6.10) 
to extract the number at the end of the line below. Convert the 
extracted value to a floating point number and print it out.

"""

text = "X-DSPAM-Confidence:    0.8475";
cpos = text.find(':')
rawstr = text[cpos + 1:]
#print(rawstr)
cleanstr = rawstr.strip()
#print(cleanstr)
answer = float(cleanstr)
print(answer)
