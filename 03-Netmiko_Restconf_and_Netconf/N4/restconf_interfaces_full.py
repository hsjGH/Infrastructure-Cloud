import requests
import json

# SSL waarschuwingen uitschakelen (self-signed certs)
requests.packages.urllib3.disable_warnings()

# --- Configuratie variabelen ---
IP_HOST = "192.168.56.101"
RESTCONF_USERNAME = "cisco"
RESTCONF_PASSWORD = "cisco123!"
DATA_FORMAT = "application/yang-data+json"

LOOPBACK_INTERFACE = "Loopback11"   # Naam van de loopback interface
LOOPBACK_IP = "10.1.1.11"           # IP-adres voor de loopback

# --- RESTCONF URLs ---
api_url_put = f"https://{IP_HOST}/restconf/data/ietf-interfaces:interfaces/interface={LOOPBACK_INTERFACE}"
api_url_get = f"https://{IP_HOST}/restconf/data/ietf-interfaces:interfaces"

# --- Headers en authenticatie ---
headers = { "Accept": DATA_FORMAT, "Content-type": DATA_FORMAT }
basicauth = (RESTCONF_USERNAME, RESTCONF_PASSWORD)

# --- YANG configuratie payload voor PUT request ---
yangConfig = {
    "ietf-interfaces:interface": {
        "name": LOOPBACK_INTERFACE,
        "description": f"RESTCONF => {LOOPBACK_INTERFACE}",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": LOOPBACK_IP,
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}

# --- Stap 1: PUT request om de loopback interface aan te maken ---
resp_put = requests.put(
    api_url_put,
    json=yangConfig,
    auth=basicauth,
    headers=headers,
    verify=False
)

# Response controleren
if 200 <= resp_put.status_code <= 299:
    print(f"STATUS OK: {resp_put.status_code} - {LOOPBACK_INTERFACE} aangemaakt")
else:
    print("ERROR bij aanmaken van interface")
    print(resp_put.status_code)
    print(resp_put.text)

# --- Stap 2: GET request om alle interfaces op te halen ---
resp_get = requests.get(
    api_url_get,
    auth=basicauth,
    headers=headers,
    verify=False
)

# JSON response prettifyen en printen
try:
    response_json = resp_get.json()
    print(json.dumps(response_json, indent=4))
except json.JSONDecodeError:
    print("Kan JSON niet decoderen:")
    print(resp_get.text)
