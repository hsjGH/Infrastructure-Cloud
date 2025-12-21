import requests 
import urllib.parse 

geocode_url = "https://graphhopper.com/api/1/geocode?"
route_url = "https://graphhopper.com/api/1/route?" 
loc1 = "Roma, Italia" 
loc2 = "Baltimore, Maryland" 
key = "04fcc0a0-c84a-4b17-a319-da1acdd784fd"

url = geocode_url + urllib.parse.urlencode({"q":loc1, "limit": "1", "key":key})

replydata = requests.get(url) 
json_data = replydata.json() 
json_status = replydata.status_code 
print(json_data) 