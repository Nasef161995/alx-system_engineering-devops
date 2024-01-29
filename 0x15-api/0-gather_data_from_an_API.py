#!/usr/bin/python3
"""returns information about his/her TODO list progress."""
import requests
import sys

if __name__ == "__main__":
    link = f"https://jsonplaceholder.typicode.com/users/"
    response = requests.get(link + sys.argv[1])

    data = response.json()
    # name of user
    name = data['name']
    # to do list
    response = requests.get(link + sys.argv[1] + "/todos")
    data = response.json()

    done_tasks = []
    for task in data:
        if task['completed'] is True:
            done_tasks.append(task['title'])

    done = len(done_tasks)
    total = len(data)
    print(f"Employee {name} is done with tasks({done}/{total}):")
    for element in done_tasks:
        print(f"\t {element}")
