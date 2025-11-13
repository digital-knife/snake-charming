#!/usr/bin/env python3

import sys

if len(sys.argv) < 3:
    print(
        "Incorrect usgage.. syntax is: python3 args_practice.py <name> <favorite_language>"
    )
    sys.exit(1)

name = sys.argv[1]

favorite_language = sys.argv[2]

print(f"Your name is {name} and your favorite language is {favorite_language}")
