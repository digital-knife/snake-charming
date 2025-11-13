#!/usr/bin/env python3

import os
import platform

report_file = "sysinfo.txt"

with open(report_file, "w") as f:
    f.write("System Report\n")
    f.write("===============\n")
    f.write(f"OS: {platform.system()} {platform.release()}\n")
    f.write(f"Working Directory: {os.getcwd()}\n")
    f.write(f"Current User is: {os.getenv('USER')}\n")

lines_read = 0
with open(report_file, "r") as f:
    for line in f:
        print(line.strip())
        lines_read += 1

print(f"Lines Read:{lines_read}")
