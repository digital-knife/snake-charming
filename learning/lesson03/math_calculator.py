#!/usr/bin/env python3

import subprocess

# run df -h

result = subprocess.run(["df", "-h", "/"], capture_output=True, text=True, check=True)
print(result)
lines = result.stdout.splitlines()

for line in lines[1:]:
    parts = line.split()
    if len(parts) > 5 and parts[5] == "/":
        used = parts[2]  # e.g "50G"
        total = parts[1]  # e.g 100G
        percent = parts[4]
        break

percent_clean = percent.rstrip("%")
disk_usage = float(percent_clean)

print(f"Disk usage (/): {disk_usage}")
