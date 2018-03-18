
# 1. prompt for a location
# 2. contact a web service and retrieve JSON for the web service
# 3. parse that data and retrieve the first place_id from the JSON

import json
import urllib.request, urllib.parse, urllib.error

BASE_URL = 'http://py4e-data.dr-chuck.net/geojson?'

while True:
    location = input('Enter location: ')
    #location = 'Arizona State University'
    if len(location) < 1 : break
    url = BASE_URL + urllib.parse.urlencode({'address': location})
    print('Retreiving',url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retreived', len(data), 'characters')
    js = json.loads(data)
    # print(json.dumps(js, indent=4))
    place_id = js['results'][0]['place_id']
    #place_id = js['results'][0]['formatted_address']['place_id']
    print('Place id', place_id)
    #break
