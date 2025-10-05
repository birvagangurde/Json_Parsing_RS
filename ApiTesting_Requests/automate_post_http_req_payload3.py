

# We'll add the book in this case: ------------------------------------------------------------------------

# Base URL: -

import requests

# this time our http method is Post

addBook_response = requests.post('http://216.10.245.166/Library/Addbook.php', json={

"name":"Learn Appium Automation with Java",
"isbn":"bhdc",
"aisle":"2fc27",
"author":"John foe"
}, headers={'Content-Type': "application/json"}
)

# The combination should be unique of the json code added otherwise it will state the book already exists
# We have given parameters here for post method and also took the first json code in Library API doc

print(addBook_response.json())

response_json = addBook_response.json()

print(type(response_json))
