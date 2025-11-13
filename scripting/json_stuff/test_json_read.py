#!/usr/bin/env python3

import json

try:
    with open("config.json", "r") as file:  # open file in read mode
        config = json.load(file)  # parse json into python-readable dictionary
    print("Config read successfully:")
    print(config)
    print(f"Server: {config['server']}")  # accessing dict key
    print(f"Disk Threshold: {config['disk_threshold']}")
except FileNotFoundError:
    print("Error: config.json not found, check file exists at location")
except json.JSONDecodeError:
    print("Error: invalid json format")
except Exception as exc:
    print(f"Error: {exc}")
