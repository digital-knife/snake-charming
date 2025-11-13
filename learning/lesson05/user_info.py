#!/usr/bin/env python3

import argparse

# 1 create parser logic
parser = argparse.ArgumentParser(description="Collect basic user info")

# 2 add arguments (all positional)
parser.add_argument("name", help="User's name")
parser.add_argument("age", help="User's age")
parser.add_argument("city", help="City where user was born")

# 3 parse them
args = parser.parse_args()

# 4 use the parsed data
print(f"Hello {args.name}, age {args.age}, from {args.city}!")
