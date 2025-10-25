#!/usr/bin/env python3

import os
import platform

print("=== System Check ===")

system = platform.system().lower()

if system == "linux":
    print("Running on Linux - perfect for servers.")
elif system == "darwin":
    print("Running on macOS - good for development.")
elif system == "windows":
    print("Running on windows - not good for anything")
else:
    print("unknown system: {system}")

print()

# check envars
env_vars = ("HOME", "SHELL", "PATH")

for var in env_vars:
    value = os.environ.get(var)
    if value:
        print(f"{var} is set and is {value}")
    else:
        print(f"{var} is MISSING!")

print()

# a modest while loop example

print("Counting down before exit:")
count = 3
while count > 0:
    print(count)
    count -= 1
print("Done")