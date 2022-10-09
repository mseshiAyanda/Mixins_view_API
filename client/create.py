import requests

endpoint = "http://127.0.0.1:8003/api/"

data = {
    "tittle": "Bible",
    "author": "nobody knows",
}

get_response = requests.post(endpoint, json=data)

print(get_response.json())