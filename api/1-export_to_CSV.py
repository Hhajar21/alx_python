#!/usr/bin/python3
"""Fetches information from JSONplaceholder API and exports to CSV"""

import csv
import requests
import sys

def export_to_csv(user_id):
    main_url = "https://jsonplaceholder.typicode.com"
    todo_url = f"{main_url}/users/{user_id}/todos"
    user_url = f"{main_url}/users/{user_id}"

    try:
        todo_response = requests.get(todo_url)
        todo_response.raise_for_status()  # Raise an exception for HTTP errors

        user_response = requests.get(user_url)
        user_response.raise_for_status()

        todo_data = todo_response.json()
        user_data = user_response.json()

        # Create a list of dictionaries with the desired data
        todo_list = []
        for todo in todo_data:
            todo_dict = {
                "USER_ID": user_id,
                "USERNAME": user_data["username"],
                "TASK_COMPLETED_STATUS": str(todo["completed"]),
                "TASK_TITLE": todo["title"]
            }
            todo_list.append(todo_dict)

        # Export the data to a CSV file
        filename = f"{user_id}.csv"
        with open(filename, 'w', newline='') as csv_file:
            fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            writer.writeheader()  # Write the header row
            writer.writerows(todo_list)  # Write the data

        print(f"Data exported to {filename}")

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
