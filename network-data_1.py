# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 07:45:04 2018

@author: Randy
"""

# URL = 'Uniform Resource Locator'
# protocol:host/document
# body of standards IETF 'Internet Engineering Task Force' www.ietf.org
# RFC 'Request For Comment' documents define the individual protocols
# RFC 2616 = HTTP 'Hypertext Transfer Protocol

# telnet www.dr-chuck.com 80
# GET http://www.dr=chuck.com/page1.htm HTTP/1.0
# returns metadata headers and HTML body text

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
# .encode() method converts Unicode strings in python to UTF-8 
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    # data = mysock.recv(512)
    data = mysock.recv(1024)    
    if (len(data) < 1):
        break
    print(data.decode())
# print(type(data))
# print(len(data))
mysock.close()