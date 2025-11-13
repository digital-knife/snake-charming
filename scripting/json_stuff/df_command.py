#!/usr/bin/env python3

import subprocess

command = ["df", "-h"]

# run above command with parameters
result = subprocess.run(command, capture_output=True, text=True)

# get the output
output = result.stdout
print("Disk Usage:")
print(output)
