#!/usr/bin/env python3

import sys
import os
import platform

#print python version
print("Python version:")
print(sys.version)
print()

#pwd
print("Current working directory:")
print(os.getcwd())
print()

#print os info
print("Operating System info:")
print(platform.system(), platform.release(), sep=" ----------------------- ")
print()

#print envars
print("Environment Variables:")
for key, value in os.environ.items():
    if key in ("HOME", "PATH"):
        print(f"{key} = {value}")
    