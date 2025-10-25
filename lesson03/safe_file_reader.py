#!/usr/bin/env python3

import os
logfile = "server.log"

print(f"=== Checking for file: {logfile} ===")

# step 1: check if file exists
if not os.path.exists(logfile):
    print("Log file not found, creating a dummy one...")
    with open(logfile, "w") as f:
        f.write("INFO: System started \n")
        f.write("WARNING: Disk space low\n")
        f.write("ERROR: Failed to connect to DB\n")

# step 2: safely read file line-by-line
try:
    with open(logfile, "r") as f:
        print("\n=== Log Contents ===")
        for line in f:
            # use .strip() to clean up newlines/spaces
            print(line.strip())

except FileNotFoundError:
    print("File does not exist")
except PermissionError:
    print("Permission denied when trying to read file")
except Exception as e:
    print(f"Unexpected error: {e}")