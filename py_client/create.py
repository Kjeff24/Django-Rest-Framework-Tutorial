import requests

headers = {'Authorization': 'Bearer dd95aeb394b702a8479e673e171f68bdcc22bde6'}

endpoint = 'http://127.0.0.1:8000/api/products/'

get_response =requests.post(endpoint, json={"title": "Every day work"}, headers=headers)

print(get_response.json())