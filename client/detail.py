import requests

endpoint = "http://127.0.0.1:8003/api/3/"

get_response = requests.get(endpoint)

print(get_response.json())