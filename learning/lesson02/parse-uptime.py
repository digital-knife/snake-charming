#!/usr/bin/env python3

import subprocess

result = subprocess.run(["uptime"], capture_output=True, text=True, check=True)

output = result.stdout
print(f"Raw output: {output}")

# Parse load average
parts = output.split("load average:")
load_part = parts[1]
print(load_part)
loads = load_part.split(",")
load_1min = float(loads[0].strip())
load_5min = float(loads[1].strip())
load_15min = float(loads[2].strip())

print(f"1-minute load average: {load_1min:.2f}")
print(f"5-minute load average: {load_5min:.2f}")
print(f"15-minute load average: {load_15min:.2f}")

# #!/usr/bin/env python3

# import subprocess

# result = subprocess.run(["uptime"], capture_output=True, text=True, check=True)
# output = result.stdout

# print(f"Raw: {output}")

# # --- BUG IS BELOW ---
# parts = output.split("load average:")
# load_part = parts[1]
# loads = load_part.split(",")
# load_1min = float(loads[0].strip())  # <-- ERROR HERE
# # --- END BUG ---

# print(f"1-minute load: {load_1min:.2f}")
