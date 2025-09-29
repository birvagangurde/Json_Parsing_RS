# ****** Parse content present in Json file

import json

with open('C:\\Users\\BIRVA\\Downloads\\BackEndAutomation_Part1\\BackEndAutomation\\course.json') as f:
    data = json.load(f)
    print(data)
    print(type(data))
    print(data['courses'][1]['title'])
    print(data['dashboard']['website'])
    print(type(data['dashboard']))


    '''
    load() → works with file objects
    loads() → works with strings
    '''