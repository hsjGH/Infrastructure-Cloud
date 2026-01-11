import json  # Module voor JSON conversie
import requests  # HTTP requests module

api_url = "http://localhost:58000/api/v1/ticket"  # URL van de API endpoint

# Headers voor request
headers = {
    "content-type": "application/json"
}

# Body van POST request: gebruikersnaam en wachtwoord
body_json = {
    "username": "cisco",
    "password": "cisco123!"
}

# Verstuur POST request naar API, zet body om naar JSON string
resp = requests.post(api_url, json.dumps(body_json), headers=headers, verify=False)

# Print HTTP status code
print("Ticket request status: ", resp.status_code)

# Parse response JSON
response_json = resp.json()

# Haal serviceTicket uit response
serviceTicket = response_json["response"]["serviceTicket"]

# Print het ticket
print("The service ticket number is: ", serviceTicket)
