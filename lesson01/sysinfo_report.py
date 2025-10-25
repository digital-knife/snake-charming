#!/usr/bin/env python3

import sys
import os

print("=== Python Info ===")
print("Executable:")
print(sys.executable)
print("Version:")
print(sys.version)

print("=== System Info ===")
print("Hostname:")
print(os.uname())
print("Working Directory:")
print(os.getcwd())

print("=== Environment ===")
for key, value in os.environ.items():
    if key in ("SHELL", "LOGNAME", "PATH"):
        print(f"{key} = {value}")

print (f"Total environment variables: {len(os.environ)}")