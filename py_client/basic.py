import requests


endpoint = 'http://127.0.0.1:8000/api/'

get_response =requests.post(endpoint, json={"content": "Hey there"})

print(get_response.json())