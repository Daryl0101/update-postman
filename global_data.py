from enum import Enum
import os

# Global variables
postmanApiKey = os.environ.get('POSTMAN_APIKEY')

class Environ(Enum):
    local = 1
    staging = 2

Path = {
    1 : {
        'url': os.environ.get('URL_LOCAL'),
        'collectionUid': os.environ.get('COLLECTION_UID_LOCAL'),
        'collectionName': os.environ.get('COLLECTION_NAME_LOCAL')
    },
    2 : {
        'url': os.environ.get('URL_STAGING'),
        'collectionUid': os.environ.get('COLLECTION_UID_STAGING'),
        'collectionName': os.environ.get('COLLECTION_NAME_STAGING')
    }
}