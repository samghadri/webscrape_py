import json

data = '''[
    { 
    "id" : "007",
    "author" : "sam",
    "size" : "l"
    },
    {
    "id" : "008",
    "author" : "arash",
    "size" : "m"
        
    }          
]'''


result = json.loads(data)
print("number of users: ", len(result))

for item in result:
    print('the authors are: ', item['author'])
    print('the sizes are: ', item['size'])