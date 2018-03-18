# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 09:48:04 2018

@author: Randy
"""

# Service Oriented Architecture provides a common service layer
# API Apllication Programming Interface
# specifications for using data

# example Google Geocoding API
# http://maps.googleapis.com/maps/api/geocode/json?address=Ann+Arbor%2c+MI
# the '+' is a space, the '%2c' is a comma 

import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
my_api_key = '&key=AIzaSyBbsE9lJCh1_NDotxYvA0ddtzV_lRgEMKs'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
        
    url = serviceurl + urllib.parse.urlencode({'address' : address}) + my_api_key
    
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    
    try:
        js = json.loads(data)
    except:
        js = None
        
    if not js or 'status' not in js or js['status'] != 'OK' :
        print('=== Failure to retrieve===')
        print(data)
        continue
    
    print(json.dumps(js, indent=4))

    lat = js['results'][0]["geometry"]["location"]["lat"]
    lng = js['results'][0]["geometry"]["location"]["lng"]
    location = js['results'][0]['formatted_address']
    print('lat', lat, 'lng', lng)
    print(location)

# had to get this manually from Google Geocode API
# YOUR API KEY: AIzaSyBbsE9lJCh1_NDotxYvA0ddtzV_lRgEMKs
# append URL with this: &key=YOUR_API_KEY

# Also, check out the python client library for the Google Maps API:
# https://github.com/googlemaps/google-maps-services-python
