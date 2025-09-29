import json


# o	JSON is stored inside a Python string (in quotes)
courses = '{"name": "RahulShetty", "languages": ["Java", "Python"]}'
print(courses[0])

# Loads method parse json string and returns dictionary
#Now you can access values with keys.


# Parsing API responses (usually JSON strings → use loads)
dict_courses = json.loads(courses)

print(type(dict_courses))
print(dict_courses)
print(dict_courses['name'])

# get me the first language taught by trainer

list_language = dict_courses['languages']
print(type(list_language))
print(list_language[0])
print(dict_courses['languages'][0])

# This is one way of json parsing