import urllib.request, urllib.parse, urllib.error
import twurl
import json

urltwitter = 'https://api.twitter.com/1.1/friends/list.json'

while True:
    print('')
    twit_account = input('Enter Your Twitter Account')
    if len(twit_account) < 0:
        break
    url = twurl.argument(urltwitter, {'screen_name': twit_account, 'count': '5'})
    print('retrieving: ', url)
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    print('the_remaining: ', headers['x-rate-limit-remaining'])
    js = json.loads(data)
    print(json.dumps(js, indent=4))

    for u in js['users']:
        print(u['screen_name'])
        s = u['status']['text']
        print(' ',s[:50])
