#!/usr/bin/python3
"""Fetches information from JSONplaceholder API and exports to JSON"""

import json
import requests
import sys

def export_to_json(user_id):
    main_url = "https://jsonplaceholder.typicode.com"
    todo_url = f"{main_url}/users/{user_id}/todos"
    user_url = f"{main_url}/users/{user_id}"

    try:
        # Fetch todo data
        todo_response = requests.get(todo_url)
        todo_response.raise_for_status()  # Raise an exception for HTTP errors
        todo_data = todo_response.json()

        # Fetch user data
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()

        if not todo_data:
            print("No tasks found for this user.")
            return

        # Create a dictionary with the desired format
        user_dict = {
            user_id: [{"task": todo["title"], "completed": todo["completed"], "username": user_data["username"]} for todo in todo_data]
        }

        # Export the data to a JSON file
        filename = f"{user_id}.json"
        with open(filename, 'w') as json_file:
            json.dump(user_dict, json_file, indent=4)

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
        export_to_json(user_id)
