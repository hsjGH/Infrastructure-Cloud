import requests

API_KEY = "cisco|7tUq72zasT4sSYQNjrM5GO0KPe0n3SDPeQ6TcnXRAJU"
ID = 11111111
TITLE = "Test2"
AUTHOR = "Tester2"
URL = "http://library.demo.local/api/v1/books"

headers = {
    "X-API-KEY": API_KEY,
    "Content-Type": "application/json"
}

data = {
    "id": ID,
    "title": TITLE,
    "author": AUTHOR
}

response = requests.post(URL, json=data, headers=headers)
print(type(response))
print(response.status_code)