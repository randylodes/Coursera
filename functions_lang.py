# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 07:41:53 2017

@author: Randy
"""

def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'en':
        print('Hello')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print ('Hi There..')

greet('es')

greet('en')

greet('fr')

greet('alien')

