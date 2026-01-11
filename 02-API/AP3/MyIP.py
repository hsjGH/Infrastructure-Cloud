import requests
from datetime import datetime  # kortere import

# Print huidige datum en tijd
print("Current date and time:")
print(datetime.now())

# API call naar publieke IP-check service
try:
    response = requests.get('http://api.myip.com/', timeout=5)  # timeout toegevoegd
    if response.status_code == 200:
        data = response.json()  # JSON response naar dict
        ip_address = data.get('ip')  # publieke IP
        country = data.get('country')  # land
        country_code = data.get('cc')  # landcode
        print(f"Public IP Address: {ip_address}")
        print(f"Country: {country}")
        print(f"Country Code: {country_code}")
    else:
        print(f"Fout bij API request, status code: {response.status_code}")
except requests.RequestException as e:
    print(f"Request failed: {e}")
