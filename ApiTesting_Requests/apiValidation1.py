import requests
import json

response = requests.get('http://216.10.245.166/Library/GetBook.php',
             params={'AuthorName': 'Rahul Shetty2'} )

print(response.text)
print(type(response.text))  #This was our first API automation: getting books by author using Python


# Now we have JSOn response in string format, so we all know how to
# convert this json string into dictionary to parse this json string into dict
# Ultimately, we want to verify if the ISBN returned by Rahul Shetty2 is PSRS.”
# LETS say our requirement automation is where this authors books should all have isbn as psrs only


dict_response = json.loads(response.text)

print(dict_response)
print(type(dict_response))

print(dict_response[0]['isbn'])


json_response = response.json()
print(type(json_response))
print(json_response[0]['isbn'])

# •	Use .json() for simpler parsing.
# •	Print response and type → know what you are handling.
# •	API automation = first step → sending request → getting response → parsing → verifying.
# •	JSON can be list inside dictionary; indexing matters.
# •	Optional arguments: headers, etc. → only if required.
