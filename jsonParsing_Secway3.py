# 26th Video - Parsing complex json

import json

# ****** Parse content present in Json file
with open('C:\\Users\\BIRVA\\Downloads\\BackEndAutomation_Part1\\BackEndAutomation\\course.json') as f:
    data = json.load(f)
    print(data)
    print(type(data))
    print(data['courses'][1]['title'])
    print(data['dashboard']['website'])
    print(type(data['dashboard']))
    print(type(data['courses']))

    # The price of course "RPA"

    for course in data['courses']:
        print(course)
        if course['title'] == "RPA":
            print(course['price'])
            assert course['price'] == 45


