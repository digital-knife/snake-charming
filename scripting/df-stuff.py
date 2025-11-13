#!/usr/bin/env python3

import subprocess

result = subprocess.run(["du", "-sh", "/home"], capture_output=True, text=True)
lines = result.stdout.splitlines()

for line in lines:
    if "/home" in line:
        print(f"HOME: {line}")
    else:
        print("Home not found..")
