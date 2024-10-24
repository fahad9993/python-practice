import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USER_NAME")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Habit Track Graph",
    "unit": "commit",
    "type": "int",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(response.text)
