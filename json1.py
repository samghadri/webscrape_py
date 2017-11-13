import json

data = '''{
        "name" : "sam",
        "phone" : {
        "type" : "intl",
        "number" : " +44 7972349822"
    },
        "email" : {
        "hide" : "yes"     
    }
}'''

result = json.loads(data)

print('the name is: ', result['name'])
print('Email Hidden?', result['email']['hide'])