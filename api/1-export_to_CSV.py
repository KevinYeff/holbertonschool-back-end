#!/usr/bin/python3
"""Script that uses a REST API and request for a given
employee ID and returns information about his/her TODO
list progress. It also exports data to a CSV file."""
import csv
import requests
from sys import argv

# Using global variables
EMPLOYEE_NAME = ''
EMPLOYEE_ID = None
NUMBER_OF_DONE_TASKS = 0
TOTAL_NUMBER_OF_TASKS = 0
TASK_TITLE = []


def get_api_response():
    """This function will gather and print data from an API."""
    global EMPLOYEE_NAME, EMPLOYEE_ID, NUMBER_OF_DONE_TASKS
    global TOTAL_NUMBER_OF_TASKS, TASK_TITLE
    # Request users
    user_request = requests.get('https://jsonplaceholder.typicode.com/users')
    # Request todos
    todos_request = requests.get('https://jsonplaceholder.typicode.com/todos')
    # Extract user id that matches employee id to extract the name
    EMPLOYEE_ID = int(argv[1])
    for user in user_request.json():
        if user['id'] == EMPLOYEE_ID:
            EMPLOYEE_NAME = user['username']
            break

    all_task_titles = []
    completed_task_titles = []

    # Extract the tasks completed
    for task in todos_request.json():
        if task['userId'] == EMPLOYEE_ID:
            all_task_titles.append(task['title'])
            if task['completed']:
                completed_task_titles.append(task['title'])
                NUMBER_OF_DONE_TASKS += 1
            TOTAL_NUMBER_OF_TASKS += 1

    # Print the format
    print('Employee {} is done with tasks({}/{}):'
          .format(EMPLOYEE_NAME,
                  NUMBER_OF_DONE_TASKS,
                  TOTAL_NUMBER_OF_TASKS))
    # Print tab + todos completed
    for title in TASK_TITLE:
        print('\t {}'.format(title))

    # Export data to CSV
    export_to_csv(EMPLOYEE_ID, EMPLOYEE_NAME, all_task_titles, completed_task_titles)

def export_to_csv(user_id, user_name, all_task_titles, completed_task_titles):
    """Export data to a CSV file."""
    csv_file_name = f'{user_id}.csv'
    with open(csv_file_name, mode='w', newline='') as file:
        # quoting
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for title in all_task_titles:
            completed_status = "True" if title in completed_task_titles else "False"
            writer.writerow([user_id, user_name, completed_status, title])

# Make sure the script doesn't execute when imported
if __name__ == '__main__':
    get_api_response()
