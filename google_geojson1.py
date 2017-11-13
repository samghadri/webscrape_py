import urllib.request, urllib.parse, urllib.error
import json


urlservice = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Please Enter The Location: ')
    if len(address) < 1: break
    url = urlservice + urllib.parse.urlencode({'address': address})
    print('Retrieving: ', url)
    x = urllib.request.urlopen(url)
    data = x.read().decode()
    print('We Retrieved: ', len(data), 'Number of Characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js['status'] != 'OK':
        print('**** Failed To Retrieve the DATA ****')
        print(data)

        continue

    print(json.dumps(js, indent=4))
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print('location')
