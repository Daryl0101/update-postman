from enum import Enum
import os

# Global variables
postmanApiKey = str(os.environ.get('POSTMAN_APIKEY'))
collectionUid = os.environ.get('COLLECTION_UID')
collectionName = str(os.environ.get('COLLECTION_NAME'))
localUrl = os.environ.get('LOCAL_URL')
localPort = os.environ.get('LOCAL_PORT')
stagingUrl = os.environ.get('STAGING_URL')
stagingPort = os.environ.get('STAGING_PORT')

class Environ(Enum):
    local = 1
    staging = 2

Path = {
    1 : f'https://{localUrl}:{localPort}/swagger/v2/swagger.json',
    2 : f'http://{stagingUrl}:{stagingPort}/swagger/v2/swagger.json'
}