#!/usr/bin/env python3

import subprocess

result = subprocess.run(["df", "-h"], capture_output=True, text=True, check=True)
lines = result.stdout.splitlines()

for line in lines:
    if "tmpfs" in line:
        continue
    if "/" in line:
        print(line)
        break
