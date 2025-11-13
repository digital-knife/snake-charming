#!/usr/bin/env python3

import subprocess

result = subprocess.run(["df", "-h"], capture_output=True, text=True, check=True)
output = result.stdout

lines = output.splitlines()

for line in lines:
    if "tmpfs" in line:
        print(line)
