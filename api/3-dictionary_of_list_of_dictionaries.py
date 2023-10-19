#!/usr/bin/python3
"""Script that uses a rest API and request for a given
employee ID and returns information about his/her TODO
list progress"""
# libraries
import json
import requests
# using the global variables

EMPLOYEE_ID = None
NUMBER_OF_DONE_TASKS = 0
TOTAL_NUMBER_OF_TASKS = 0
TASK_TITLE = []
EMPLOYEE_USERNAME = ''
EMPLOYEES = None
TASK_COMPLETED_STATUS = ''


def get_api_response():
    """This function will gather and print data from an API."""
    global EMPLOYEES, TASK_TITLE

    # Request users
    user_request = requests.get('https://jsonplaceholder.typicode.com/users')
    # Request todos
    todos_request = requests.get('https://jsonplaceholder.typicode.com/todos')
    EMPLOYEES = user_request.json()
    TASK_TITLE = todos_request.json()
    # Export all data to JSON
    export_all_to_json(EMPLOYEES, TASK_TITLE)


def export_all_to_json(users, tasks):
    """This function will export all data to JSON."""
    global EMPLOYEE_ID, NUMBER_OF_DONE_TASKS
    global TOTAL_NUMBER_OF_TASKS, TASK_TITLE, EMPLOYEE_USERNAME
    global TASK_COMPLETED_STATUS

    # Creating a dictionary to organize tasks
    all_employee_data = {}
    for user in users:
        EMPLOYEE_ID = user['id']
        EMPLOYEE_USERNAME = user['username']
        TOTAL_NUMBER_OF_TASKS = []
        for task in tasks:
            if task['userId'] == EMPLOYEE_ID:
                TASK_TITLE = task['title']
                TASK_COMPLETED_STATUS = task['completed']
                TOTAL_NUMBER_OF_TASKS.append({"username": EMPLOYEE_USERNAME,
                                              "task": TASK_TITLE,
                                              "completed": TASK_COMPLETED_STATUS})

        all_employee_data[EMPLOYEE_ID] = TOTAL_NUMBER_OF_TASKS


    # Write all the data to a json file
    with open(f'todo_all_employees.json', 'w') as jsonfile:
        json.dump(all_employee_data, jsonfile, indent=4)


if __name__ == '__main__':
    # Get the API response
    get_api_response()
