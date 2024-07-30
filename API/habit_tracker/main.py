import requests
import json
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

pixela_endpoint = os.getenv('PIXELA_END_POINT')

USER = os.getenv('USER')
TOKEN = os.getenv('TOKEN')
GRAPH_ID = os.getenv('GRAPH_ID')

quantity = input("How many minutes you spent while coding today: ")
description = input("Worked on which Python topic: ")
operation = input("Enter which operation you need to perform (Create/Update/Delete) for pixel: ").lower()
today = datetime.now().strftime("%Y%m%d")

headers = {
    "X-USER-TOKEN": TOKEN,
}


def create_user():
    parameters = {
        "token": TOKEN,
        "username": USER,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    response = requests.post(pixela_endpoint, json=parameters)
    print(response.text)


def create_graph():
    graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"
    graph_config = {
        "id": GRAPH_ID,
        "name": "Daily Coding Graph",
        "unit": "min",
        "type": "float",
        "color": "shibafu",
    }
    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)


def create_pixel():
    pixel_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}"
    pixel_config = {
        "date": today,
        "quantity": quantity,
        "optionalData": json.dumps({
            "description": f"Worked on {description}",
            "language": "Python"
        }),
    }
    response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
    print(response.text)


def update_pixel():
    update_pixel_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}/{today}"
    update_config = {
        "quantity": quantity,
        "optionalData": json.dumps({
            "description": f"Worked on {description}",
            "language": "Python"
        }),
    }
    response = requests.put(url=update_pixel_endpoint, json=update_config, headers=headers)
    print(response.text)


def delete_pixel():
    delete_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}/{today}"
    response = requests.delete(url=delete_endpoint, headers=headers)
    print(response.text)


def main():
    if operation == "create":
        create_pixel()
    elif operation == "update":
        update_pixel()
    elif operation == "delete":
        delete_pixel()
    else:
        print("Invalid operation. Please enter 'Create', 'Update', or 'Delete'.")


if __name__ == "__main__":
    main()
