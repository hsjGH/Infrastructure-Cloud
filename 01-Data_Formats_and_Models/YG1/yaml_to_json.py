# yaml_to_json.py
import yaml
import json

# ---- 1. YAML input bestand ----
yaml_file = "rack_structure.yaml"  # dit bestand moet bestaan
with open(yaml_file, "r") as f:
    yang_data = yaml.safe_load(f)  # laad YAML in Python dict (YANG-like)

# ---- 2. Print ingelezen data ----
print("---- YANG STRUCTURE LOADED FROM YAML ----")
print(yang_data)

# ---- 3. Conversie naar JSON ----
json_file = "rack_structure.json"
with open(json_file, "w") as f:
    json.dump(yang_data, f, indent=4)  # JSON met indent voor leesbaarheid

print(f"YAML is geconverteerd naar JSON en opgeslagen in {json_file}")

# ---- 4. Optioneel: print JSON string ----
json_str = json.dumps(yang_data, indent=4)
print("---- JSON OUTPUT ----")
print(json_str)
