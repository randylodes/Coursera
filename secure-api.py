# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 11:19:51 2018

@author: Randy
"""

import urllib.request, urllib.parse, urllib.error
import twurl  # Dr Chuck's own code; uses oauth lib and hidden.py (you write)
import json

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if acct == 'quit': break
    if len(acct) < 1: acct = 'RandyLodes'
    url = twurl.augment(TWITTER_URL, {'screen_name' : acct, 'count' : '5'})
    print('Retrieving:', url)
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)
    print(json.dumps(js, indent=4))
    
    for u in js['users']:
        print(u['screen_name'])
        s = u['status']['text']
        print('  ', s[:50])

