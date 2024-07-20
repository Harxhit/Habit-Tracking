import requests
import datetime as dt
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Constants from environment variables
USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")
GRAPH_ID = os.getenv("GRAPH_ID")
today = dt.datetime.now()

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_value_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
update_endpoint = f"{graph_value_endpoint}/{today.strftime('%Y%m%d')}"

user_parameter = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Uncomment the following lines to create the user if it does not exist yet
# response = requests.post(url=pixela_endpoint, json=user_parameter)
# response.raise_for_status()
# print(response.text)

headers = {
    "X-USER-TOKEN": TOKEN
}

# Create a new graph
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai",
}

# Uncomment the following lines to create the graph if it does not exist yet
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

graph_value_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}

# Uncomment the following lines to post a new value if it does not exist yet
# response = requests.post(url=graph_value_endpoint, json=graph_value_config, headers=headers)
# print(response.text)

new_value = {
    "quantity": "50.577"
}

response = requests.put(url=update_endpoint, json=new_value, headers=headers)
print(response.text)
