import urllib.request, urllib.parse, urllib.error
import json
count = list()

while True:

    url = input('Please Enter your URL:')
    if len(url) < 1:
        break
    print('Retrieving..', url)
    connection = urllib.request.urlopen(url)
    data = connection.read()
    print('We Retrieved',len(data),'characters')

    try:
        js = json.loads(data)
    except:
        js = None
    comment = js['comments']

    for com in comment:
        count.append(com['count'])
    print('Count', len(comment))
    print('Sum: ', sum(count))