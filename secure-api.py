# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 11:19:51 2018

@author: Randy
"""

# Some APIs require authorization, eg Twitter uses OAuth protocol
# https://developer.twitter.com/en/docs/basics/authentication/overview/oauth

# I had to install oauth on my Anaconda setup; failed after multiple attempts 
# conda install -c conda-forge python-oauth2
# but this wouldn't install until I did this:
# conda install -c anaconda cryptography
# continued trouble loading oauth2
# help("modules") to list all available modules
# still not installed -- may try manual install later



import urllib.request, urllib.parse, urllib.error
import twurl  # Dr Chuck's own code; uses oauth lib and hidden.py (you write)
import json

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if len(acct) < 1: break
    url = twurl.augment(TWITTER_URL, {'screen_name' : acct, 'count' : '5'})
    print('Retrieving:', url)
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-liimit-remaining'])
    js = json.loads(data)
    print(json.dumps(js, indent=4))
    
    for u in js['users']:
        print(u['screen_name'])
        s = u['status']['text']
        print('  ', s[:50])

