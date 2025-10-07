# We'll have to delete the book in the part
import json
import configparser

from utilities.resources import ApiResources
from GlobalProperties_OAuthMechanism.pAuthentication_APIs_AuthMethod.utilities.configurations import *
from end_to_end_payload1 import *

import requests

# before
# config = configparser.ConfigParser()
# config.read('utilities/properties.ini')
# config['API']['endpoint']

# after
url = getConfig()['API']['endpoint'] + ApiResources.addBook
headers = {'Content-Type': "application/json"}
addBook_response = requests.post(url, verify=False, json=addBookPayload("bhdt"),
                                 headers=headers
                                 )

# The combination should be unique of the json code added otherwise it will state the book already exists
# We have given parameters here for post method and also took the first json code in Library API doc

print(addBook_response.json())

response_json = addBook_response.json()
print(type(response_json))

bookID = response_json['ID']
print(bookID)

# Delete Book: ------------------------------------------------------------------------------------------------------------

response_deleteBook = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={

    "ID": bookID

}, headers={'Content-Type': "application/json"}
                                    )

print("Status Code:", response_deleteBook.status_code)

assert response_deleteBook.status_code == 200

res_json = response_deleteBook.json()

print(res_json["msg"])

assert res_json["msg"] == "book is successfully deleted"



url = 'https://api.github.com/user'

github_response = requests.get(url, auth=('sanjanamesh', getPassword()))

print(github_response.status_code)