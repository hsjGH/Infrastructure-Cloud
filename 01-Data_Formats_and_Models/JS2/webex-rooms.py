# Fill in this file with the rooms/spaces listing code from the Webex Teams exerciseimport requests
import json

# -------- Config ----------
access_token = "<Vul hier je access token in>"
url_rooms = "https://api.ciscospark.com/v1/rooms"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# -------- API Call: haal alle rooms op --------
response = requests.get(url_rooms, headers=headers)
rooms_data = response.json()  # JSON response

# Print ruwe JSON (optioneel)
# print(json.dumps(rooms_data, indent=2))

# -------- Filter: toon enkel rooms met 'KVR' in de naam --------
filtered_rooms = [
    room for room in rooms_data.get("items", [])
    if "KVR" in room.get("title", "")
]

# -------- Print gefilterde resultaten --------
print("Gefilterde Webex Rooms:")
for room in filtered_rooms:
    print(f"- {room['title']} (ID: {room['id']})")

