####  DELETE WEBEX "DEMO" SPACES
from webexteamssdk import WebexTeamsAPI
### Access Token 12 hours: https://developer.webex.com/docs/api/getting-started (login required)
access_token = "OWZlZjFmMmUtM2FjNi00NjU5LWFkNDUtMzJlZDZkMzFiZjVmNWE4Zjc0ODEtMDdi_PE93_56361a18-ee8a-4da6-a728-ee9b2cd9887b"
api = WebexTeamsAPI(access_token=access_token)
# Find all rooms that should be removed
all_rooms = api.rooms.list()

demo_rooms = [room for room in all_rooms if 'GROUP_KVR_' in room.title]

# Delete all of the demo rooms
for room in demo_rooms:
    print("Deleting ... " + room.title)
    api.rooms.delete(room.id)