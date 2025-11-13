#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("usage: python3 writer.py <filename>")
    sys.exit(1)

filename = sys.argv[1]
message = input("Enter a message to write: ")

with open(filename, "w") as f:
    f.write(message + "\n")

print(f"Message saved to {filename}")
