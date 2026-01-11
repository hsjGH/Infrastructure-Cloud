import requests
import json

### Access Token: geldig 12 uur, nodig voor Webex API calls
access_token = "OWZlZjFmMmUtM2FjNi00NjU5LWFkNDUtMzJlZDZkMzFiZjVmNWE4Zjc0ODEtMDdi_PE93_56361a18-ee8a-4da6-a728-ee9b2cd9887b"

# Structuur van groepen en leden, als dict
groups_struc = {
 "groups": [
      { "group": { "group_id": "G1" , "group_name": "GROUP_KVR_A" ,    
                   "members": [   
                     {"person_id": "P-1" , "person_name": "Gergely", "email": "nickgergely@biasc.be"},
                     {"person_id": "P-2" , "person_name": "Sacha", "email": "sacha@biasc.be"},
                     {"person_id": "P-3" , "person_name": "Lisa", "email": "lisa@biasc.be"} 
                   ]
                 }
      },
      { "group": { "group_id": "G2" , "group_name": "GROUP_KVR_B" ,    
                   "members": [   
                     {"person_id": "P-4" ,"person_name": "Lucas", "email": "lucasn@biasc.be"}, 
                     {"person_id": "P-5" ,"person_name": "Lukas", "email": "Lukas@biasc.be"}, 
                     {"person_id": "P-6" ,"person_name": "Ken", "email": "ken@biasc.be"} 
                   ]     
                 }
      },
   ]
}

# Webex API endpoint voor rooms
url = 'https://api.ciscospark.com/v1/rooms'

# Headers met bearer token
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}

# Loop over groepen
for rec in groups_struc["groups"]:
    create_group_name = rec["group"]["group_name"]
    print("Creating ... " + create_group_name)

    # Maak nieuwe room aan
    payload_space = {"title": create_group_name}
    res_space = requests.post(url, headers=headers, json=payload_space)

    # Haal ID van nieuwe room op
    NEW_SPACE_ID = res_space.json()["id"]  # Let op: crash als POST faalt

    # Voeg elk lid toe aan de room
    for mbr in rec["group"]["members"]:
        room_id = NEW_SPACE_ID
        person_email = mbr["email"]
        url2 = 'https://api.ciscospark.com/v1/memberships'
        payload_member = {'roomId': room_id, 'personEmail': person_email}
        res_member = requests.post(url2, headers=headers, json=payload_member)
