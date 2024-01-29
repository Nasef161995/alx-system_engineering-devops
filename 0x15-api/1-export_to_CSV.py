#!/usr/bin/python3
"""returns information about his/her TODO list progress."""
import requests
import sys
import csv


if __name__ == "__main__":
    link = f"https://jsonplaceholder.typicode.com/users/"
    response = requests.get(link + sys.argv[1])

    data = response.json()
    # name of user
    name = data['name']
    # to do list
    response = requests.get(link + sys.argv[1] + "/todos")
    data = response.json()

    filename = sys.argv[1] + ".csv"
    with open(filename, 'w', newline='') as csvfile:
        fileWriting = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)

        for row in data:
            fileWriting.writerow([sys.argv[1], name,
                                  row.get('completed'), row.get('title')])
