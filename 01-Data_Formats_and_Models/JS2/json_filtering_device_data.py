import json

# ---- PLACEHOLDERS / YANG STRUCTURE ----
inventory_dict = {}
inventory_list = []
rack_struc = {"rack": []}
dev_dict = {}
dev_list = []
interface_dict = {}
interface_list = []

# ---- RACK STRUCTURE DATA ----
rack_struc = {
 "rack": [
      { "device": { "dev_id": "D1",
                    "dev_name": "R1",
                    "role": "router",
                    "interfaces": [
                      {"interface": "GigabitEthernet1", "ipaddress": "10.0.1.1", "subnet_mask": "255.255.255.0"},
                      {"interface": "GigabitEthernet2", "ipaddress": "10.0.3.1", "subnet_mask": "255.255.255.0"},
                      {"interface": "GigabitEthernet3", "ipaddress": "10.0.4.1", "subnet_mask": "255.255.255.0"}
                     ]
                 }
      },
      { "device": { "dev_id": "D2",
                    "dev_name": "C1",
                    "role": "core",
                    "interfaces": [
                     {"interface": "VLAN1", "ipaddress": "10.0.1.2", "subnet_mask": "255.255.255.0"},
                     {"interface": "VLAN2", "ipaddress": "10.0.2.1", "subnet_mask": "255.255.255.0"},
                     {"interface": "VLAN20", "ipaddress": "10.0.20.1", "subnet_mask": "255.255.255.0"}
                   ]
                 }
      },
      { "device": { "dev_id": "D3",
                    "dev_name": "AC",
                    "role": "access",
                    "interfaces": [
                     {"interface": "VLAN2", "ipaddress": "10.0.2.2", "subnet_mask": "255.255.255.0"}
                   ]
                 }
      }
   ]
}

# ---- 1. RAW PRINT ----
print('------1: RAW DICT---------')
print(type(rack_struc))
print(rack_struc)

# JSON-string print
js_struc = json.dumps(rack_struc, indent=4)
print('------1B: JSON FORMAT--------')
print(js_struc)

# ---- 2. INSPECT FIRST DEVICE ----
g = rack_struc["rack"][0]
print('------2: FIRST DEVICE KEYS------')
print(type(g))
print(g["device"].keys())

# ---- 3. LOOP THROUGH DEVICES & INTERFACES ----
print('------3: DEVICE NAMES & INTERFACES------')
for g in rack_struc["rack"]:
    print(f"Device Name: {g['device']['dev_name']}, Role: {g['device']['role']}")
    for intf in g["device"]["interfaces"]:
        print(f"  Interface: {intf['interface']}, IP: {intf['ipaddress']}, Subnet: {intf['subnet_mask']}")

# ---- 4. CHECK KEYS ----
last_dev = rack_struc["rack"][-1]["device"]
print('------4: KEYS DEVICE------')
print(last_dev.keys())
print('------4A: KEYS INTERFACE------')
print(last_dev["interfaces"][0].keys())
