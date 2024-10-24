import requests
import os
from dotenv import load_dotenv

load_dotenv()

PIXELA_ENDP0INT = "https://pixe.la/v1/users"

user_params = {
    "token": os.getenv("TOKEN"),
    "username": os.getenv("USER_NAME"),
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDP0INT, json=user_params)
# print(response.text)
