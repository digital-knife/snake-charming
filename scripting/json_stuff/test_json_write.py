#!/usr/bin/env python3

import json

config = {"server": "db01", "port": 5432, "enabled": False}

try:
    with open("new_config.json", "w") as file:
        json.dump(config, file, indent=4)
    print("Config written to new_config.json")
except Exception as exc:
    print(f"Error encountered writing JSON: {exc}")
