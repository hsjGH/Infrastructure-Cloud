#!/usr/bin/env python3
"""
Simple API demo: GET request to JSONPlaceholder
"""

import requests

# URL van de API
url = "https://jsonplaceholder.typicode.com/posts/1"

# GET request
response = requests.get(url)

# Statuscode checken
if response.status_code == 200:
    data = response.json()  # JSON naar dict
    print("Title:", data['title'])
    print("Body:", data['body'])
else:
    print("Error:", response.status_code)
