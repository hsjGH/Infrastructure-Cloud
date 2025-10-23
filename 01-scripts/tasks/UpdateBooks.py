import requests

API_KEY = "cisco|7tUq72zasT4sSYQNjrM5GO0KPe0n3SDPeQ6TcnXRAJU"
URL = "http://library.demo.local/api/v1/books/1"

headers = {
    "accept": "application/json",
    "X-API-KEY": $API_KEY,
    "Content-Type": "application/json"
}

data = {
    "id": 0,
    "title": "string",
    "author": "string"
}

response = requests.put(URL, json=data, headers=headers)
print(response.json())
