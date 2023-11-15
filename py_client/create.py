import requests


endpoint = 'http://127.0.0.1:8000/api/products/'

get_response =requests.post(endpoint, json={"title": "Every day work"})

print(get_response.json())