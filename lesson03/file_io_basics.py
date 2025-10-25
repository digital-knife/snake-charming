#!/usr/bin/env python3

#create and write to a new file
with open("example.txt", "w") as f:
    f.write("Hello from Python!\n")
    f.write("This file was created automatically.\n")

# read the file back
with open("example.txt", "r") as f:
    content = f.read()

print("=== File Content ===")
print(content)

#append to the same file
with open("example.txt", "a") as f:
    f.write("Appending one more line.\n")

# verify by reading again
with open("example.txt", "r") as f:
    print("=== Updated File ===")
    print(f.read())