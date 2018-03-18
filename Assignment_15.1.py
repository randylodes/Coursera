
# The program will prompt for a URL, read the JSON data from that URL using urllib
# and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file
# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_56525.json (Sum ends with 23)

import json
import urllib.request, urllib.parse, urllib.error

while True:
    url = input('Enter the URL:')
    if len(url) < 1: break


    # url = 'http://py4e-data.dr-chuck.net/comments_42.json'
    # url = 'http://py4e-data.dr-chuck.net/comments_56525.json'

    print('Retrieving:', url)

    # Setup the connection and retrieve the raw data
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()

    # Load the data as a JSON object
    js = json.loads(data)
    # print(json.dumps(js, indent=4))

    # Use a for loop to extract all the comment count data and sum it
    comment_sum = 0
    for comment in js['comments']:
        # print(comment)
        count = int(comment['count'])
        # print(count)
        comment_sum = comment_sum + count
    print('Count:', len(js['comments']))
    print('Sum:', comment_sum)








# Sample format:
# {
#   comments: [
#     {
#       name: "Matthias"
#       count: 97
#     },
#     {
#       name: "Geomer"
#       count: 97
#     }
#     ...
#   ]
# }
