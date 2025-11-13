# #!/usr/bin/env python3

# percent = "75%"
# number = float(percent.rstrip("%"))
# print(f"Usage: {number}%")

#!/usr/bin/env python3
disk = "85%"
usage = float(disk.rstrip("%"))

if usage > 80:
    print("High Disk!")
else:
    print("OK")
