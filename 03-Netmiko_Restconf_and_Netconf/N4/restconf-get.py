import json
import requests

# SSL warnings uitschakelen
requests.packages.urllib3.disable_warnings()

# URL voor de RESTCONF GET request
api_url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces"

# Headers om JSON te ontvangen/versturen
headers = {
    "Accept": "application/yang-data+json",
    "Content-type": "application/yang-data+json"
}

# Basis-authenticatie
basicauth = ("cisco", "cisco123!")

# GET request sturen
resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
print(resp)  # HTTP status code

# JSON response omzetten naar Python dict
response_json = resp.json()

# Mooi printen
print(json.dumps(response_json, indent=4))
