#!/usr/bin/python3

import requests
import sys

link = "https://jsonplaceholder.typicode.com/users/"

response = requests.get(link + sys.argv[1])

if response.status_code == 200:
    data = response.json()
    # Process the response data
    print(data.get('name'))
    print( f"Employee {data['name']} is done with tasks(/):")

else:
    print("Request failed with status code:", response.status_code)
