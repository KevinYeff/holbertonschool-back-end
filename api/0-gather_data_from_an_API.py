#!/usr/bin/python3
"""Script that uses a rest API and request for a given
employee ID and returns information about his/her TODO
list progress"""
# libraries
import requests
from sys import argv
# using the global variables
EMPLOYEE_NAME = ''
EMPLOYEE_ID = None
NUMBER_OF_DONE_TASKS = 0
TOTAL_NUMBER_OF_TASKS = 0
TASK_TITLE = []


def get_api_response():
    """This function will gather and print data from a API"""
    global EMPLOYEE_NAME, EMPLOYEE_ID, NUMBER_OF_DONE_TASKS
    global TOTAL_NUMBER_OF_TASKS, TASK_TITLE
    # request users
    user_request = requests.get('https://jsonplaceholder.typicode.com/users')
    # request todos
    todos_request = requests.get('https://jsonplaceholder.typicode.com/todos')
    # extract user id that matches employee id to extract the name
    EMPLOYEE_ID = int(argv[1])

    for user in user_request.json():
        if user['id'] == EMPLOYEE_ID:
            EMPLOYEE_NAME = user['name']
            break

    # extract the task completed
    for task in todos_request.json():
        if task['userId'] == EMPLOYEE_ID:
            if task['completed']:
                TASK_TITLE.append(task['title'])
                NUMBER_OF_DONE_TASKS += 1
            TOTAL_NUMBER_OF_TASKS += 1
    # print the format
    print('Employee {} is done with tasks({}/{}):'.format(EMPLOYEE_NAME,
                                                          NUMBER_OF_DONE_TASKS,
                                                          TOTAL_NUMBER_OF_TASKS))
    # print tab + todos completed
    for title in TASK_TITLE:
        print('\t {}'.format(title))

# make sure script doesn't execute when imported
if __name__ == '__main__':
    get_api_response()
  