#!/usr/bin/python3
"""fetches information from JSONplaceholder API and exports to JSON"""

import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    todo_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    try:
        todo_response = requests.get(todo_url)
        todo_response.raise_for_status()

        user_response = requests.get(user_url)
        user_response.raise_for_status()

        todo_data = todo_response.json()
        user_data = user_response.json()

        todo_list = []
        for todo in todo_data:
            todo_dict = {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": user_data["username"],
            }
            todo_list.append(todo_dict)

        with open(f"{user_id}.json", "w") as json_file:
            json.dump({user_id: todo_list}, json_file, indent=4)

        print(f"Data exported to {user_id}.json")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
