import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = ""
USERNAME = ""
GRAPH_ID = ""

user_params = {
    "token": "1234567890",
    "username": "tumba",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ichou",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": f"{today.strftime('%Y%m%d')}",
    "quantity": input("How many kilometers did you cycle today?: "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#
# new_pixel_data = {
#     "quantity": "90.16",
# }
#
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)
