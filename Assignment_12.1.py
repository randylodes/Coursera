# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 09:44:27 2018

@author: Randy
"""

#==============================================================================
# Exploring the HyperText Transport Protocol
# You are to retrieve the following document using the HTTP protocol in a way 
# that you can examine the HTTP Response headers.
# http://data.pr4e.org/intro-short.txt
#==============================================================================

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    # data = mysock.recv(512)
    data = mysock.recv(1024)    
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()
