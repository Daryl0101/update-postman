'''
It is best to leave this file untouched
'''

import requests
import json
import os
import global_data
from loader import Loader

# Environment choice validation
def ValidateEnvironmentChoice(choice):
    enumValues = [i.value for i in global_data.Environ]
    if choice not in enumValues:
        raise ValueError('Invalid environment!')

# Prompt environment input from user
print('Environments')
for i in global_data.Environ:
    print(i.value, ':', i.name)
choice = int(input('Select the environment: '))
ValidateEnvironmentChoice(choice)

# Download latest version of openapi json file
url = global_data.Path[choice]['url']
response = requests.get(url, verify = False)
data = response.json()
with open('files/swagger.json', 'w') as f:
    json.dump(data, f)
f.close()

# Convert openapi format to Postman collections format (pretty)
os.system('openapi2postmanv2 -s "files/swagger.json" -o "files/new-swagger.json" -p')

# Amend data in converted file
convertedFile = open('files/new-swagger.json', 'r')
convertedData = json.load(convertedFile)
convertedFile.close()

convertedData = {
    'collection':{
        'info':{
            "name": global_data.Path[choice]['collectionName'],
            "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
        },
        'item': convertedData['item']
    }
}

# Declare Request Body
newData = json.dumps(convertedData)

# Declare Request Headers
headers = {
    'X-Api-Key': global_data.postmanApiKey,
    'Postman-Token': '<calculated when request is sent>',
    'Content-Length': '<calculated when request is sent>',
    'Host': '<calculated when request is sent>',
    'User-Agent': 'PostmanRuntime/7.32.2',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/json'
}

# Loading animation
loader = Loader('Postman update in progress...').start()

# Send request
response = requests.put(
    f'https://api.getpostman.com/collections/{global_data.Path[choice]["collectionUid"]}',
    data = newData,
    headers = headers
)

loader.stop()

# Output response
print('\nStatus :', response.status_code)
print('Response body :', response.text)