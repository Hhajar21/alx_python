#!/usr/bin/python3
"""fetches information from JSONplaceholder API and exports to CSV"""

from csv import DictWriter, QUOTE_ALL
from requests import get
from sys import argv


if __name__ == "__main__":
    main_url = "https://jsonplaceholder.typicode.com"
    todo_url = main_url + "/user/{}/todos".format(argv[1])
    name_url = main_url + "/users/{}".format(argv[1])
    todo_result = get(todo_url).json()
    name_result = get(name_url).json()

    todo_list = []
    for todo in todo_result:
        todo_dict = {}#!/usr/bin/python3
"""Fetches information from JSONplaceholder API and exports to CSV"""

import csv
import requests
import sys

def export_to_csv(user_id):
    main_url = "https://jsonplaceholder.typicode.com"
    todo_url = f"{main_url}/users/{user_id}/todos"
    name_url = f"{main_url}/users/{user_id}"
    
    try:
        todo_response = requests.get(todo_url)
        todo_response.raise_for_status()  # Raise an exception for HTTP errors
        
        name_response = requests.get(name_url)
        name_response.raise_for_status()
        
        todo_data = todo_response.json()
        name_data = name_response.json()
        
        # Create a list of dictionaries with the desired data
        todo_list = [{"USER_ID": user_id, "USERNAME": name_data["username"],
                      "TASK_COMPLETED_STATUS": str(todo["completed"]),
                      "TASK_TITLE": todo["title"]} for todo in todo_data]
        
        # Export the data to a CSV file
        with open(f"{user_id}.csv", 'w', newline='') as csv_file:
            fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            
            writer.writeheader()  # Write the header row
            writer.writerows(todo_list)  # Write the data
        
        print(f"Data exported to {user_id}.csv")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py USER_ID")
    else:
        user_id = sys.argv[1]
        export_to_csv(user_id)

        todo_dict.update({"user_ID": argv[1], "username": name_result.get(
            "username"), "completed": todo.get("completed"),
                          "task": todo.get("title")})
        todo_list.append(todo_dict)
    with open("{}.csv".format(argv[1]), 'w', newline='') as f:
        header = ["user_ID", "username", "completed", "task"]
        writer = DictWriter(f, fieldnames=header, quoting=QUOTE_ALL)
        writer.writerows(todo_list)