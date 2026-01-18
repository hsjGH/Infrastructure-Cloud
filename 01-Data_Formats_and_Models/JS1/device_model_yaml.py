# device_model_yaml.py
import yaml

# ---- 1. DEFINITIE VAN DEVICE MODEL (YANG-LIKE) ----
device_model = {
    "device": {
        "dev_id": "D1",
        "dev_name": "R1",
        "role": "router",
        "interfaces": [
            {
                "interface": "GigabitEthernet1",
                "description": "Uplink to Core",
                "ip_address": "10.0.1.1",
                "subnet_mask": "255.255.255.0"
            },
            {
                "interface": "GigabitEthernet2",
                "description": "LAN Network",
                "ip_address": "10.0.2.1",
                "subnet_mask": "255.255.255.0"
            },
            {
                "interface": "GigabitEthernet3",
                "description": "Management",
                "ip_address": "10.0.3.1",
                "subnet_mask": "255.255.255.0"
            }
        ]
    }
}

# ---- 2. Opslaan naar YAML bestand ----
yaml_file = "device_model.yaml"
with open(yaml_file, "w") as f:
    yaml.dump(device_model, f, sort_keys=False)  # sort_keys=False = volgorde behouden

print(f"Device model opgeslagen in {yaml_file}")

# ---- 3. Print YAML output (optioneel) ----
yaml_str = yaml.dump(device_model, sort_keys=False)
print("---- DEVICE MODEL YAML ----")
print(yaml_str)
