#!/usr/bin/python3


"""
Using what you did in the task #0, extend your
 Python script
to export data in the CSV format.
"""
import csv
import requests
import sys

if __name__ == '__main__':
    sessionReq = requests.Session()

    idEmp = sys.argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(idEmp)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(idEmp)

    employee = sessionReq.get(idURL)
    employeeName = sessionReq.get(nameURL)

    json_req = employee.json()
    usr = employeeName.json()['username']

    totalTasks = 0

    for donetasks in json_req:
        if donetasks['completed']:
            totalTasks += 1

    csvfile = idEmp + '.csv'

    with open(csvfile, 'w', newline='') as file:
        conv_file = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for i in json_req:
            conv_file.writerow([idEmp, usr, i.get('completed'), i.get('title')])    


