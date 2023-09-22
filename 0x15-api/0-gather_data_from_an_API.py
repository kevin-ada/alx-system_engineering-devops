#!/usr/bin/python3

"""
Write a Python script that, using this REST API,
 for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests

import sys

if __name__ == '__main__':
    Todo_URI = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(Todo_URI)
    todo_data = response.json()
    total = 0
    completed = 0
    tasks = []
    User_response = requests.get('https://jsonplaceholder.typicode.com/users')
    user_data = User_response.json()

    for i in user_data:
        if i.get('id') == int(sys.argv[1]):
            employee = i.get('name')

    for i in todo_data:
        if i.get('userId') == int(sys.argv[1]):
            total += 1

            if i.get('completed') is True:
                completed += 1
                tasks.append(i.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(employee, completed,
                                                          total))

    for i in tasks:
        print("\t {}".format(i))