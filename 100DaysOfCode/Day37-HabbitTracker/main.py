import requests
from datetime import datetime

USERNAME = "kazi"
TOKEN = "gdfgdfg444hjk653453"
GRAPH_ID = "graph1"

USER_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{USER_ENDPOINT}/{USERNAME}/graphs"
PIXEL_CREATION_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"

user_body = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

create_user = requests.post(url=USER_ENDPOINT, json=user_body)

graph_body = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Hour",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

create_graph = requests.post(url=GRAPH_ENDPOINT, json=graph_body, headers=headers)

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you invested into coding today? "),
}

update_graph = requests.post(url=PIXEL_CREATION_ENDPOINT, json=pixel_data, headers=headers)

#graph - example:
#https://pixe.la/v1/users/kazi/graphs/graph1.html