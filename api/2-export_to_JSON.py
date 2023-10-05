#!/usr/bin/python3
"""Fetches information from JSONplaceholder API and exports to JSON"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py USER_ID")
        sys.exit(1)

    user_id = sys.argv[1]
    main_url = "https://jsonplaceholder.typicode.com"
    todo_url = f"{main_url}/users/{user_id}/todos"
    user_url = f"{main_url}/users/{user_id}"

    try:
        todo_response = requests.get(todo_url)
        todo_response.raise_for_status()

        user_response = requests.get(user_url)
        user_response.raise_for_status()

        todo_data = todo_response.json()
        user_data = user_response.json()

        task_list = [{"task": task["title"], "completed": task["completed"], "username": user_data["username"]} for task in todo_data]
        
        with open(f"{user_id}.json", "w") as json_file:
            json.dump({user_id: task_list}, json_file)

        print(f"Data exported to {user_id}.json")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
