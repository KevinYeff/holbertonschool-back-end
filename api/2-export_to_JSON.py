#!/usr/bin/python3
"""Script that uses a rest API and request for a given
employee ID and returns information about his/her TODO
list progress"""
# libraries
import json
import requests
from sys import argv
# using the global variables
EMPLOYEE_NAME = ''
EMPLOYEE_ID = None
NUMBER_OF_DONE_TASKS = 0
TOTAL_NUMBER_OF_TASKS = 0
TASK_TITLE = []
EMPLOYEE_USERNAME = ''


def get_api_response():
    """This function will gather and print data from an API."""
    global EMPLOYEE_NAME, EMPLOYEE_ID, NUMBER_OF_DONE_TASKS
    global TOTAL_NUMBER_OF_TASKS, TASK_TITLE, EMPLOYEE_USERNAME
    # Request users
    user_request = requests.get('https://jsonplaceholder.typicode.com/users')
    # Request todos
    todos_request = requests.get('https://jsonplaceholder.typicode.com/todos')
    # Extract user id that matches employee id to extract the name
    EMPLOYEE_ID = int(argv[1])
    for user in user_request.json():
        if user['id'] == EMPLOYEE_ID:
            EMPLOYEE_NAME = user['name']
            EMPLOYEE_USERNAME = user['username']
            break

    # Get all task titles
    all_task_titles = []
    for task in todos_request.json():
        if task['userId'] == EMPLOYEE_ID:
            all_task_titles.append(task)

    # Export data to JSON
    export_to_json(EMPLOYEE_ID, all_task_titles)


def export_to_json(employee_id, all_task_titles):
    """This function will export data to JSON."""
    # Create a JSON object
    json_data = {
        employee_id: []
    }

    for task in all_task_titles:
        json_data[employee_id].append({
            "task": task["title"],
            "completed": task["completed"],
            "username": EMPLOYEE_USERNAME,
        })

    # Write the JSON object to a file
    with open(f'{employee_id}.json', 'w') as jsonfile:
        json.dump(json_data, jsonfile, indent=4)


if __name__ == '__main__':
    # Get the API response
    get_api_response()
