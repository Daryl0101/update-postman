from enum import Enum
import os

# Global variables
postmanApiKey = str(os.environ.get('POSTMAN_APIKEY'))
collectionUid = os.environ.get('COLLECTION_UID')
collectionName = str(os.environ.get('COLLECTION_NAME'))
localUrl = os.environ.get('LOCAL_URL')
stagingUrl = os.environ.get('STAGING_URL')

class Environ(Enum):
    local = 1
    staging = 2

Path = {
    1 : f'{localUrl}',
    2 : f'{stagingUrl}'
}